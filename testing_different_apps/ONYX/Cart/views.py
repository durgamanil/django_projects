from django.shortcuts import render

# Create your views here.
def Cart_home(request):
    
    return render(request, "home.html",{})
