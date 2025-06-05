from django.urls import path
from . import views

urlpatterns = [
    path('enrollment/', views.enrollment_list, name='enrollment-list'),
    path('enrollment/<int:pk>/', views.enrollment_detail, name='enrollment-detail'),
]
