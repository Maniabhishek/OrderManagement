from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Dashboard(request):
    return render(request,'accounts/dashboard.html')

def Products(request):
    return render(request,'accounts/products.html')

def Customer(request):
    return render(request,'accounts/customer.html')