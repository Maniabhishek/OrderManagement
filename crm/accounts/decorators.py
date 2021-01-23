from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('Dashboard')
        else:
            return view_func(request,*args,**kwargs)
        
    return wrapper_func


def allowed_user(allowed_roles=[]):
    def decorators(view_func_original):
        def wrapper_func(request,*args,**kwargs):
            group =None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                
                return view_func_original(request,*args,**kwargs)
            else:
                return HttpResponse("you are not authorized to see the page ")
        return wrapper_func
    return decorators
    

def admin_only(view_func_original):
    def wrappers(request,*args,**kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'customer':
            return redirect('userPage')
        if group== 'admin':
            return view_func_original(request,*args,**kwargs)
        
    return wrappers
