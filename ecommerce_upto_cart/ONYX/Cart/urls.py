
from django.conf.urls import url
from .views import (
    Cart_home,
    cart_update,
    checkout_home,
    checkout_done_view
    )

urlpatterns = [
    url(r'^$',Cart_home,name='cart_home'),
    url(r'^checkout/success/$', checkout_done_view, name='success'),
    url(r'^checkout/$', checkout_home, name='checkout'),
    url(r'^update/$', cart_update, name='update'),
]