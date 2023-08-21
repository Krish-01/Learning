from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    text = """<h1> Hey There!!! This is Krish </h1>"""
    return HttpResponse(text)
