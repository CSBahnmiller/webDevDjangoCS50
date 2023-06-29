from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def conrad(request):
    return HttpResponse("Conrad is Awesome!!")

def silas(request):
    return HttpResponse("Silas is super awesome!!")

def greet(request, name):
    return render(request, "Hello/greet.html", {
        "name": name.capitalize()
    })