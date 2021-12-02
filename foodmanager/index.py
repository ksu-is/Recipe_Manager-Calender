from django.http import HttpResponse
from django.shortcuts import render

def myplate(request):
    return render(request,'myplate.html')