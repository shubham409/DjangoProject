
from django import views
from django.contrib import admin
from django.urls import path , include
from .views import multiple_objects, single_object, users
urlpatterns = [
    
    path('users/',users),
    path('single/',single_object),
    path('multiple/',multiple_objects),
]