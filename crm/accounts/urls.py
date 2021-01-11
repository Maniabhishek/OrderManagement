from django.contrib import admin
from django.urls import path ,include
from .views import Dashboard,Customer,Products

urlpatterns = [
    path('',Dashboard,name='Dashboard'),
    path('customer/',Customer,name = 'Customer'),
    path('products/',Products,name='products'),

]
