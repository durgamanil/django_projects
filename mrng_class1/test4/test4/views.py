from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>this is workingsjdfkjksdfhsadkfhadss</h1>")

def index(request):
    return HttpResponse("<h1>this is indexxxxxxx</h1>")