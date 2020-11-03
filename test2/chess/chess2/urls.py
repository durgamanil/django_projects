from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.home, name='home'),
    #path('^', views.index,name='index'),

    #url(r'^(?P<student_sno>[0-9]+)/$', views.detail, name='detail'),
    url(r'^$', views.detail, name='detail'),
]