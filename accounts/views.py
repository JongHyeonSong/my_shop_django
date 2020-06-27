from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('now home')

def products(request):
    return HttpResponse('now products')

def customer(request):
    return HttpResponse('now customer')