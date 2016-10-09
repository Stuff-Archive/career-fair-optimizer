from django.shortcuts import render

# Create your views here.
# Functions that handle the data

#use enviornment variables to store keys
#logic

from django.http import HttpResponse

def sillyMessage(request):
    return HttpResponse("Hello, world. You're at the polls index.")
