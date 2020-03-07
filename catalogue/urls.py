from django.urls import path
from .views import index, ajax_cart


urlpatterns = [
    path('', index),
    path('ajax_cart', ajax_cart)
]
