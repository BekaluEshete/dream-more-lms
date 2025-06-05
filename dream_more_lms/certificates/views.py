from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Certificate
from .serializers import CertificateSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Certificate List View
@swagger_auto_schema(
    method='GET',
    responses={
        200: CertificateSerializer(many=True),
    }
)
@swagger_auto_schema(
    method='POST',
    request_body=CertificateSerializer,
    responses={
        201: CertificateSerializer,
        400: openapi.Response('Bad Request', examples={'application/json': {'error': 'Invalid data'}})
    }
)
@api_view(['GET', 'POST'])
def certificate_list(request):
    if request.method == 'GET':
        return Response(
            CertificateSerializer(Certificate.objects.all(), many=True).data
        )

    # anyone can issue a certificate by POSTing student + course IDs
    serializer = CertificateSerializer(data=request.data)
    if serializer.is_valid():
        cert = serializer.save()  # PDF is auto-generated in model
        return Response (
            CertificateSerializer(cert).data,
          
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Certificate Detail View
@swagger_auto_schema(
    method='GET',
    responses={
        200: CertificateSerializer,
        404: openapi.Response('Not Found', examples={'application/json': {'error': 'Not found'}})
    }
)
@swagger_auto_schema(
    method='DELETE',
    responses={
        204: openapi.Response('No Content'),
        404: openapi.Response('Not Found')
    }
)
@api_view(['GET', 'DELETE'])
def certificate_detail(request, pk):
    try:
        cert = Certificate.objects.get(pk=pk)
    except Certificate.DoesNotExist:
        return Response({'error': 'Not found'}, status=404)

    if request.method == 'GET':
        return Response(CertificateSerializer(cert).data)

    cert.delete()
    return Response({'message': 'Deleted'}, status=204)