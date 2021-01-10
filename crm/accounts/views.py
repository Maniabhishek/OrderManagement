from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Home(request):
    return render(request,'accounts/home.html')

def Products(request):
    return render(request,'accounts/products.html')

def Customer(request):
    return render(request,'accounts/customer.html')