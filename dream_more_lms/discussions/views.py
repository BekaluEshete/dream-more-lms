from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import Discussion, Reply
from .serializers import DiscussionSerializer, ReplySerializer
from django.core.mail import send_mail
from notifications.models import Notification
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Discussion List View
@swagger_auto_schema(
    method='GET',
    responses={
        200: DiscussionSerializer(many=True),
    }
)
@swagger_auto_schema(
    method='POST',
    request_body=DiscussionSerializer,
    responses={
        201: DiscussionSerializer,
        400: openapi.Response('Bad Request', examples={'application/json': {'error': 'Invalid data'}})
    }
)
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def discussion_list(request):
    if request.method == 'GET':
        discussions = Discussion.objects.all()
        serializer = DiscussionSerializer(discussions, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DiscussionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Add Reply View
@swagger_auto_schema(
    method='POST',
    request_body=ReplySerializer,
    manual_parameters=[
        openapi.Parameter('discussion_id', openapi.IN_PATH, description="ID of the discussion", type=openapi.TYPE_INTEGER, required=True),
    ],
    responses={
        201: ReplySerializer,
        400: openapi.Response('Bad Request', examples={'application/json': {'error': 'Invalid data'}})
    }
)
@api_view(['POST'])
@permission_classes([AllowAny])
def add_reply(request, discussion_id):
    data = request.data.copy()
    data['discussion'] = discussion_id

    serializer = ReplySerializer(data=data)
    if serializer.is_valid():
        reply = serializer.save()

        discussion = reply.discussion
        recipient = discussion.user

        # Create in-app notification
        if recipient != reply.user:
            Notification.objects.create(
                user=recipient,
                message=f"{reply.user.username} replied to your discussion: '{discussion.question[:50]}...'"
            )

            # Send email
            if recipient.email:
                send_mail(
                    subject="New reply to your discussion",
                    message=f"{reply.user.username} replied: {reply.content}\n\nView discussion: http://127.0.0.1:8000/discussions/{discussion.id}/",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[recipient.email],
                    fail_silently=True
                )

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)