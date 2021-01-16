from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.forms import inlineformset_factory #this library is responsible for creating multiple instances at one time 
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
    OrderFormSet = inlineformset_factory(Associates,Order,fields=('products','status'),extra=3) 
                    # in this case we use 1 st parameter as a parent model and then child model and then fields from child model
    customer = Associates.objects.get(id=cust_id )
    formset = OrderFormSet(queryset=Order.objects.none(), instance =customer)
    # form = OrderForm(initial={'customer':customer})
    if request.method =='POST':
        # print(request.POST)
        formset =OrderFormSet(request.POST,instance = customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context = {'formset':formset}
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