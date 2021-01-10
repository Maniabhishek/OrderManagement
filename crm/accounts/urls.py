from django.contrib import admin
from django.urls import path ,include
from .views import Home,Customer,Products

urlpatterns = [
    path('',Home,name='home'),
    path('customer/',Customer,name = 'Customer'),
    path('products/',Products,name='products'),

]
