from django.shortcuts import render
from django.http import HttpResponse

def get_method(request):
    return HttpResponse("Это страница contacts")

def get_about(request):
    return HttpResponse("Это страница about") 

def hello(request):
    header = {"name": "Alex"}
    return HttpResponse("hello", headers=header)
