import uuid
import requests
import hmac
import hashlib
import logging
import os
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Payment
from .serializers import PaymentSerializer
from courses.models import Course
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Configure logging
logger = logging.getLogger(__name__)

CHAPA_HOSTED_URL = 'https://api.chapa.co/v1/hosted/pay'
CHAPA_CHARGES_URL = 'https://api.chapa.co/v1/charges'
CHAPA_VERIFY_URL = 'https://api.chapa.co/v1/transaction/verify/'
CHAPA_WEBHOOK_SECRET = os.getenv('CHAPA_WEBHOOK_SECRET', 'your_random_webhook_secret_123456')  # Fallback from settings.py

# HTML Checkout View
@swagger_auto_schema(
    method='GET',
    manual_parameters=[
        openapi.Parameter('course_id', openapi.IN_QUERY, description="ID of the course", type=openapi.TYPE_INTEGER, required=True),
        openapi.Parameter('amount', openapi.IN_QUERY, description="Payment amount", type=openapi.TYPE_NUMBER, required=True),
    ],
    responses={200: openapi.Response('HTML Checkout Form')}
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def html_checkout(request):
    course_id = request.GET.get('course_id')
    amount = request.GET.get('amount')

    if not course_id or not amount:
        return Response({"error": "Course ID and amount are required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        course = Course.objects.get(id=course_id)
        student = request.user
        tx_ref = str(uuid.uuid4())
        Payment.objects.create(
            student=student,
            course=course,
            amount=amount,
            chapa_tx_ref=tx_ref,
            status="pending"
        )
        context = {
            'public_key': settings.CHAPA_PUBLIC_KEY,
            'tx_ref': tx_ref,
            'amount': amount,
            'currency': 'ETB',
            'email': student.email or 'user@example.com',
            'first_name': student.first_name or 'User',
            'last_name': student.last_name or 'Name',
            'title': f"Payment for {course.title}",
            'description': f"Enrollment in {course.title}",
            'callback_url': settings.CHAPA_CALLBACK_URL,
            'return_url': settings.CHAPA_RETURN_URL,
        }
        return render(request, 'payments/checkout.html', context)
    except Course.DoesNotExist:
        return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)

# Direct Charge Initiation
@swagger_auto_schema(
    method='POST',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'course_id': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the course'),
            'amount': openapi.Schema(type=openapi.TYPE_NUMBER, description='Payment amount'),
            'mobile': openapi.Schema(type=openapi.TYPE_STRING, description='Customer phone number'),
            'payment_method': openapi.Schema(type=openapi.TYPE_STRING, description='Payment method (e.g., telebirr)'),
        },
        required=['course_id', 'amount', 'mobile', 'payment_method']
    ),
    responses={
        200: openapi.Response('Charge initiated', examples={'application/json': {'message': 'Charge initiated'}}),
        400: openapi.Response('Bad Request')
    }
)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def initiate_direct_charge(request):
    course_id = request.data.get('course_id')
    amount = request.data.get('amount')
    mobile = request.data.get('mobile')
    payment_method = request.data.get('payment_method')

    if not all([course_id, amount, mobile, payment_method]):
        return Response({"error": "Missing required fields"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        course = Course.objects.get(id=course_id)
        student = request.user
        tx_ref = str(uuid.uuid4())
        Payment.objects.create(
            student=student,
            course=course,
            amount=amount,
            chapa_tx_ref=tx_ref,
            status="pending",
            payment_method=payment_method
        )

        payload = {
            'amount': str(amount),
            'currency': 'ETB',
            'tx_ref': tx_ref,
            'mobile': mobile,
        }
        headers = {
            'Authorization': f'Bearer {settings.CHAPA_SECRET_KEY}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.post(f'{CHAPA_CHARGES_URL}?type={payment_method}', data=payload, headers=headers)
        response_data = response.json()

        if response.status_code == 200 and response_data.get('status') == 'success':
            return Response(response_data)
        return Response({"error": response_data.get('message', 'Charge initiation failed')}, status=status.HTTP_400_BAD_REQUEST)
    except Course.DoesNotExist:
        return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)

# Chapa Callback (Verification)
@swagger_auto_schema(
    method='GET',
    manual_parameters=[
        openapi.Parameter('tx_ref', openapi.IN_QUERY, description="Transaction reference (also accepts 'trx_ref')", type=openapi.TYPE_STRING, required=True),
    ],
    responses={
        200: openapi.Response('Payment verified'),
        400: openapi.Response('Bad Request'),
        404: openapi.Response('Not Found')
    }
)
@api_view(['GET'])
@permission_classes([AllowAny])
def chapa_callback(request):
    logger.info(f"Callback received with params: {request.GET}")
    # Check for both 'tx_ref' and 'trx_ref' to handle Chapa's parameter naming
    tx_ref = request.GET.get('tx_ref') or request.GET.get('trx_ref')
    if not tx_ref:
        logger.error("Missing tx_ref or trx_ref in callback")
        return Response({'error': 'Missing tx_ref or trx_ref'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        payment = Payment.objects.get(chapa_tx_ref=tx_ref)
    except Payment.DoesNotExist:
        logger.error(f"Payment not found for tx_ref: {tx_ref}")
        return Response({'error': 'Payment not found'}, status=status.HTTP_404_NOT_FOUND)

    headers = {'Authorization': f'Bearer {settings.CHAPA_SECRET_KEY}'}
    verify_url = f'{CHAPA_VERIFY_URL}{tx_ref}'
    verify_response = requests.get(verify_url, headers=headers)
    verify_data = verify_response.json()

    if verify_response.status_code == 200 and verify_data.get('status') == 'success':
        payment.status = 'success'
        payment.chapa_order_id = verify_data.get('data', {}).get('id')
        payment.save()
        logger.info(f"Payment verified successfully for tx_ref: {tx_ref}")
        return redirect(settings.CHAPA_RETURN_URL)
    else:
        payment.status = 'failed'
        payment.save()
        logger.error(f"Payment verification failed for tx_ref: {tx_ref}, reason: {verify_data.get('message')}")
        return Response({'error': 'Payment verification failed'}, status=status.HTTP_400_BAD_REQUEST)

# Webhook Endpoint
@swagger_auto_schema(method='POST', responses={200: openapi.Response('Webhook received')})
@api_view(['POST'])
@permission_classes([AllowAny])
def payment_webhook(request):
    signature = request.headers.get('Chapa-Signature') or request.headers.get('x-chapa-signature')
    if not signature:
        logger.warning("Webhook received without signature")
        return HttpResponse(status=400)

    # Verify signature
    computed_signature = hmac.new(
        CHAPA_WEBHOOK_SECRET.encode('utf-8'),
        request.body,
        hashlib.sha256
    ).hexdigest()

    if not hmac.compare_digest(computed_signature, signature):
        logger.error("Webhook signature verification failed")
        return HttpResponse(status=400)

    event = request.data
    logger.info(f"Webhook event received: {event}")
    tx_ref = event.get('tx_ref')
    if tx_ref:
        try:
            payment = Payment.objects.get(chapa_tx_ref=tx_ref)
            payment.status = event.get('status', 'failed')
            payment.save()
            logger.info(f"Payment status updated via webhook for tx_ref: {tx_ref}")
        except Payment.DoesNotExist:
            logger.warning(f"No payment found for tx_ref: {tx_ref} in webhook")
            pass  # Ignore if payment not found

    return HttpResponse(status=200)

# Payment Success Page
@swagger_auto_schema(method='GET', responses={200: openapi.Response('Payment success page')})
@api_view(['GET'])
@permission_classes([AllowAny])
def payment_success(request):
    logger.info("Payment success page accessed")
    return Response({'message': 'Payment successful! You are now enrolled in the course.'})