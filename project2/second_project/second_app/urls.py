
from django.contrib import admin
from django.urls import path
from .views import reciever
urlpatterns = [
    path('webhook_reciever',reciever,name="reciever")
]
