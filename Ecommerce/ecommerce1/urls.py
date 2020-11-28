
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from .views import *
from django.conf.urls import url



urlpatterns = [
    
    url(r'^$',home_page),
]
