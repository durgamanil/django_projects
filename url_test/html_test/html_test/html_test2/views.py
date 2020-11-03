from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'home.html',{'name':'anil'})

def addition(request):
    frname=request.GET['fname']
    lsname=request.GET['lname']
    results=frname+lsname
    return render(request,'addition.html',{'result':results})
