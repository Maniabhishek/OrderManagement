from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.

def Dashboard(request):
    customers  = Associates.objects.all()
    order = Order.objects.all()
    order_count = order.count()
    order_delivered = order.filter(status ='Delivered').count()
    order_pending = order.filter(status = 'pending').count()
    
    context = {
    
        'order' : order,'customers':customers , 'order_count':order_count,'order_delivered':order_delivered , 'order_pending':order_pending
    }
    return render(request,'accounts/dashboard.html',context)


def Products(request):
    products = Product.objects.all()    
    return render(request,'accounts/products.html',{'product':products})

def Customer(request,pk_test):
    customer = Associates.objects.get(id=pk_test)
    order = customer.order_set.all()
    total_order = order.count()
    context = {'customer':customer,'order':order,'total_order':total_order}
    return render(request,'accounts/customer.html',context)


def createOrder(request,cust_id):
    customer = Associates.objects.get(id=cust_id )
    form = OrderForm()
    if request.method =='POST':
        # print(request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request,'accounts/order_form.html',context)

def updateOrder(request,pk_id):
    order = Order.objects.get(id=pk_id)
    form = OrderForm(instance=order)
    if request.method == 'POST':   
        form = OrderForm(request.POST,instance=order)
        form.save()
        return redirect('/')
    context = {'form':form}
    return render(request,'accounts/update.html',context)


def deleteOrder(request,pk):
    print("something")
    order = Order.objects.get(id=pk)
    print(order)
    if request.method=='POST':
        order.delete()
        
        return redirect('/')
    return render(request,'accounts/deleteOrder.html',{'order':order})