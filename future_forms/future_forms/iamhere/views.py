from django.shortcuts import render
#from .order_form import KartForm

def home(request):
    return render(request, 'kart/home.html')

def order(request):
    first=request.POST['firstname']
    last=request.POST['lastname']
    return render(request,'results.html')
