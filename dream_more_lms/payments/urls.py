from django.urls import path
from . import views

urlpatterns = [
    path('html-checkout/', views.html_checkout, name='html_checkout'),
    path('initiate-direct/', views.initiate_direct_charge, name='initiate_direct_charge'),
    path('callback/', views.chapa_callback, name='chapa_callback'),
    path('webhook/', views.payment_webhook, name='payment_webhook'),
    path('success/', views.payment_success, name='payment_success'),
]