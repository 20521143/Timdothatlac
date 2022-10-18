from unittest import loader
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.
def greet(request, name):
    return HttpResponse(f"Hello {name}")

def hello(request):
    template = loader.get_template('search/register.html')
    return  HttpResponse(template.render(request))


def login(request):
    return render(request, 'search/login.html')

def resetpwd(request):
    return render(request,'search/reset_password.html')

def register(request):
    return render(request,'search/register.html')
