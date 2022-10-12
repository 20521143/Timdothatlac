from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def greet(request, name):
    return HttpResponse(f"Hello {name}")

def hello(request):
    return HttpResponse("hello world")
