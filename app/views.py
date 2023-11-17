from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def kanth(request):
    return HttpResponse('<h1>kanth is drinker</h1>')