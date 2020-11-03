from django.shortcuts import render
from django.http import HttpResponse
from .models import student
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    st1=student.objects.all()
    return render(request,"index.html",{'student':st1})

def detail(request,student_sno):
    st_num=student.objects.get(pk=student_sno)
    return render(request,"chess2/detail.html",{'st_num':st_num})



