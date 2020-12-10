from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from .views import (product_list_view,ProductListView)


urlpatterns = [
    url(r'^$',ProductListView.as_view(),name="product"),
    url(r'^Products-fbv/',product_list_view,name="product-fbv"),
    #url(r'^product-fbv/$',product_list_view,name="product"),
   
    
]