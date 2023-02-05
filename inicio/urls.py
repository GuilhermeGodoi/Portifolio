from django.contrib import admin
from django.urls import path, include
from inicio.views import index

urlpatterns = [
    path('', index)
]
