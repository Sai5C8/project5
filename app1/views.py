from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def tej(request):
    return HttpResponse('<h1>tej is good</h1>')
def teja1(request):
    return render(request,'tej.html')  