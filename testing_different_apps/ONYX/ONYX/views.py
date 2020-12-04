import os
import re
from datetime import datetime

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
    now = datetime.now()
    #name="anil"
    # formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # # Filter the name argument to letters only using regular expressions. URL arguments
    # # can contain arbitrary text, so we restrict to safe characters only.
    # match_object = re.match("[a-zA-Z]+",name)

    # if match_object:
    #     clean_name = match_object.group(0)
    # else:
    #     clean_name = "Friend"

    # content = "Hello there, " + clean_name + "! It's " + formatted_now


    contact_form =  ContactForm()
    context={'name':"ONYX",
             'form':contact_form,
             'date':now,
            
            }
    if request.method =="POST":
        print(request.POST.get('fullname'))
        print(request.POST.get('email'))
        print(request.POST.get('content'))
    return render(request,'contact/contact_page.html',context)

