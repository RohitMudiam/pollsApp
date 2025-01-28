from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hi this is the landing Page of the application')

# Create your views here.
