from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context={}
    return render(request, 'accounts/dashboard.html', context)

def products(request):
    context={}
    return render(request, 'accounts/products.html', context)

def customer(request):
    context={}
    return render(request, 'accounts/customer.html', context)
