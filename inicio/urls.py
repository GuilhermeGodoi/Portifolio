from django.contrib import admin
from django.urls import path, include
from inicio.views import index, email

urlpatterns = [
    path('', index, name='index'),
    path('email/', email, name='email'),
]
