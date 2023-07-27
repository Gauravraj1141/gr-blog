from django.urls import path
from . import views

urlpatterns = [
    path('payment', views.Home.as_view(), name='payment'),
    path('payment-failed', views.Failed.as_view(), name='payment-failed'),
    path('payment-success', views.Success.as_view(), name='payment-success'),
]