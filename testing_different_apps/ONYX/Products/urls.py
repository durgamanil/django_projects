from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from .views import product_home


urlpatterns = [
    url(r'^$',product_home,name="product_home"),
    
]