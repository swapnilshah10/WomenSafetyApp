from django.contrib import admin
from django.urls import path , include
from .views1 import upload_file

urlpatterns = [
    path('list/' , upload_file , name='list')
]