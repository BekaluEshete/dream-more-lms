from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Notification
from .serializers import NotificationSerializer

# Notification List View
@swagger_auto_schema(
    method='GET',
    manual_parameters=[
        openapi.Parameter('user', openapi.IN_QUERY, description="Filter by user ID", type=openapi.TYPE_INTEGER),
    ],
    responses={
        200: NotificationSerializer(many=True),
    }
)
@swagger_auto_schema(
    method='POST',
    request_body=NotificationSerializer,
    responses={
        201: NotificationSerializer,
        400: openapi.Response('Bad Request', examples={'application/json': {'error': 'Invalid data'}})
    }
)
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])  # Allow all users
def notification_list(request):
    if request.method == 'GET':
        user_id = request.GET.get('user')
        notifications = Notification.objects.filter(user_id=user_id) if user_id else Notification.objects.all()
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = NotificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Mark Notification Read View
@swagger_auto_schema(
    method='PUT',
    manual_parameters=[
        openapi.Parameter('pk', openapi.IN_PATH, description="ID of the notification", type=openapi.TYPE_INTEGER, required=True),
    ],
    responses={
        200: openapi.Response('Success', examples={'application/json': {'message': 'Marked as read'}}),
        404: openapi.Response('Not Found', examples={'application/json': {'error': 'Notification not found'}})
    }
)
@api_view(['PUT'])
@permission_classes([AllowAny])
def mark_notification_read(request, pk):
    try:
        notification = Notification.objects.get(pk=pk)
        notification.is_read = True
        notification.save()
        return Response({'message': 'Marked as read'})
    except Notification.DoesNotExist:
        return Response({'error': 'Notification not found'}, status=status.HTTP_404_NOT_FOUND)