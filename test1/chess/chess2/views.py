from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#def home(request):
#   return HttpResponse("This is home ");

def menu(request):
    return HttpResponse("<h1>This is working menu!!!</h1>");
