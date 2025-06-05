from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import Course
from .serializers import CourseSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# ✅ Create Course / Get All Courses
@swagger_auto_schema(
    method='GET',
    manual_parameters=[
        openapi.Parameter('instructor', openapi.IN_QUERY, description="Filter by instructor ID", type=openapi.TYPE_INTEGER),
        openapi.Parameter('category', openapi.IN_QUERY, description="Filter by category ID", type=openapi.TYPE_INTEGER),
    ],
    responses={
        200: CourseSerializer(many=True),
    }
)
@swagger_auto_schema(
    method='POST',
    request_body=CourseSerializer,
    responses={
        201: CourseSerializer,
        400: openapi.Response('Bad Request', examples={'application/json': {'error': 'Invalid data'}})
    }
)
@swagger_auto_schema(
    method='DELETE',
    responses={
        204: openapi.Response('No Content'),
    }
)
@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([AllowAny])  # for all non authenticated users only
def course_list(request):
    if request.method == 'GET':
        instructor_id = request.GET.get('instructor')
        category_id = request.GET.get('category')

        courses = Course.objects.all()
        if instructor_id:
            courses = courses.filter(instructor_id=instructor_id)
        if category_id:
            courses = courses.filter(category_id=category_id)

        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # Attach instructor from authenticated user
        data = request.data.copy()
        data['instructor'] = request.user.id

        serializer = CourseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Course.objects.all().delete()
        return Response({'message': f'{count[0]} courses deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

# ✅ Retrieve, Update, Delete a specific course
@swagger_auto_schema(
    method='GET',
    responses={
        200: CourseSerializer,
        404: openapi.Response('Not Found', examples={'application/json': {'error': 'Course not found'}})
    }
)
@swagger_auto_schema(
    method='PUT',
    request_body=CourseSerializer,
    responses={
        200: CourseSerializer,
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
@permission_classes([AllowAny])  # for all authenticated non users only
def course_detail(request, pk):
    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return Response({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CourseSerializer(course, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        course.delete()
        return Response({'message': 'Course deleted successfully'}, status=status.HTTP_204_NO_CONTENT)