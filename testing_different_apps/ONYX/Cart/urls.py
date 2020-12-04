
from django.conf.urls import url
from .views import Cart_home

urlpatterns = [
    url(r'^$',Cart_home,name='cart_home'),
]