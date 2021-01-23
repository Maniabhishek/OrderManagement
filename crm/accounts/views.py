from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.forms import inlineformset_factory #this library is responsible for creating multiple instances at one time 
from .models import *
from .forms import *
from .filters import *
from django.contrib import messages
from django.contrib.auth import authenticate ,login ,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .decorators import *
from django.contrib.auth.models import Group
# Create your views here.

# def register(request):
#     form = UserCreationForm()
#     if request.method=='POST':
#         form = UserCreationForm(request.POST)
#         print(form)
#         if form.is_valid():
#             form.save()
#     context = {"form":form}
#     return render(request,'accounts/register.html',context)


def userPage(request):
    context = {}
    return render(request,'accounts/user.html',context)


@unauthenticated
def register(request):
  
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name = 'customer')
            user.groups.add(group)
            messages.success(request,'Account created for '+username)
        return redirect('login')
    context = {'form':form}
    return render(request,'accounts/register.html',context)

@unauthenticated
def loginAccount(request):
    
    if request.method == 'POST':
        user = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=user,password=password)
        if user is not None:
            login(request,user)
            return redirect('Dashboard')
        else:
            message = messages.info(request,"Username Or Password is incorrect")
            return render(request,'accounts/login.html')

    return render(request,'accounts/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')



@login_required(login_url='login')
@admin_only
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

@login_required(login_url='login')
@admin_only
def Products(request):
    products = Product.objects.all()    
    return render(request,'accounts/products.html',{'product':products})

@login_required(login_url='login')
@admin_only
def Customer(request,pk_test):
    customer = Associates.objects.get(id=pk_test)
    order = customer.order_set.all()

    myFilter = OrderFilter(request.GET,queryset=order)
    order = myFilter.qs
    total_order = order.count()
    context = {'customer':customer,'order':order,'total_order':total_order,'myFilter':myFilter}
    return render(request,'accounts/customer.html',context)


@login_required(login_url='login')
@admin_only
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

@login_required(login_url='login')
@admin_only
def updateOrder(request,pk_id):
    order = Order.objects.get(id=pk_id)
    form = OrderForm(instance=order)
    if request.method == 'POST':   
        form = OrderForm(request.POST,instance=order)
        form.save()
        return redirect('/')
    context = {'form':form}
    return render(request,'accounts/update.html',context)


@login_required(login_url='login')
@admin_only
def deleteOrder(request,pk):
    print("something")
    order = Order.objects.get(id=pk)
    print(order)
    if request.method=='POST':
        order.delete()
        
        return redirect('/')
    return render(request,'accounts/deleteOrder.html',{'order':order})