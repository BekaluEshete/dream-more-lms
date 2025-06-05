from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Enrollment
from .serializers import EnrollmentSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Enrollment List View
@swagger_auto_schema(
    method='GET',
    responses={
        200: EnrollmentSerializer(many=True),
    }
)
@swagger_auto_schema(
    method='POST',
    request_body=EnrollmentSerializer,
    responses={
        201: EnrollmentSerializer,
        400: openapi.Response('Bad Request', examples={'application/json': {'error': 'Invalid data'}})
    }
)
@api_view(['GET', 'POST'])
def enrollment_list(request):
    if request.method == 'GET':
        # Return all enrollments without any filtering
        enrollments = Enrollment.objects.all()
        serializer = EnrollmentSerializer(enrollments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # Allow student and course to be passed explicitly
        serializer = EnrollmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Enrollment Detail View
@swagger_auto_schema(
    method='GET',
    responses={
        200: EnrollmentSerializer,
        404: openapi.Response('Not Found', examples={'application/json': {'error': 'Enrollment not found'}})
    }
)
@swagger_auto_schema(
    method='PUT',
    request_body=EnrollmentSerializer,
    responses={
        200: EnrollmentSerializer,
        400: openapi.Response('Bad Request'),
        404: openapi.Response('Not Found')
    }
)
@swagger_auto_schema(
    method='DELETE',
    responses={
        204: openapi.Response('No Content'),
        404: openapi.Response('Not Found')
    }
)
@api_view(['GET', 'PUT', 'DELETE'])
def enrollment_detail(request, pk):
    try:
        enrollment = Enrollment.objects.get(pk=pk)
    except Enrollment.DoesNotExist:
        return Response({'error': 'Enrollment not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EnrollmentSerializer(enrollment)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EnrollmentSerializer(enrollment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        enrollment.delete()
        return Response({'message': 'Enrollment deleted successfully'}, status=status.HTTP_204_NO_CONTENT)