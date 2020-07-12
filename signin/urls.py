
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from signin.views import home

urlpatterns = [
    path('home', home),
]
