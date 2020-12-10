from django.views.generic import ListView
from django.shortcuts import render

from django.conf import settings
from django.http import JsonResponse
from Products.models import Product



class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "Products/product_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        print(context)
        return context

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #     cart_obj, new_obj = Cart.objects.new_or_get(self.request)
    #     context['cart'] = cart_obj
    #     return context

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     return Product.objects.all()

# Create your views here.
def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request,'Products/products_home_page.html',context)
