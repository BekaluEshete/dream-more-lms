from django.urls import path
from . import views

urlpatterns = [
    path('certificates/', views.certificate_list,   name='certificate-list'),
    path('certificates/<int:pk>/', views.certificate_detail, name='certificate-detail'),
]
