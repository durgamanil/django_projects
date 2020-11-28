from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from .forms import ContactForm

def home_page(request):
    context={'name':"ONYX"}
    return render(request,'home_page.html',context)


def about_page(request):
    context={'name':"ONYX"}
    return render(request,'home_page.html',context)


def contact_page(request):
    contact_form =  ContactForm()
    context={'name':"ONYX",
             'form':contact_form
            
            }
    return render(request,'home_page.html',context)