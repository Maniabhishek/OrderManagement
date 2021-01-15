from django.contrib import admin
from django.urls import path ,include
from .views import Dashboard,Customer,Products,createOrder, deleteOrder,updateOrder

urlpatterns = [
    path('',Dashboard,name='Dashboard'),
    path('customer/<str:pk_test>/',Customer,name = 'customer'),
    path('products/',Products,name='products'),
    path('create_order/<str:cust_id>',createOrder,name='createOrder'),
    path('update/<str:pk_id>/',updateOrder,name='update'),
    path('deleteOrder/<str:pk>/',deleteOrder,name='deleteOrder'),


]
