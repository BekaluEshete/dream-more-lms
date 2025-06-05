from django.urls import path
from .views import notification_list, mark_notification_read

urlpatterns = [
    path('notifications/', notification_list, name='notification-list'),
    path('notifications/<int:pk>/read/', mark_notification_read, name='mark-read'),
]
