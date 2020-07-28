# -*-coding:utf-8-*-
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate,login
from apitest.models import Product

# Create your views here.
#def test(request):
 #   return HttpResponse('hello test')

def login(request):
    if request.POST:
        username = password = ' '
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        if user is not None and user.is_active:
            auth.login(request,user)
            request.session['user'] = username
            response = HttpResponseRedirect('/product_manage/')
            return response
        else:
            return render(request,'login.html',{'error':'username or password error'})

    return render(request,'login.html')
   # return render(request,'login.html')

def home(request):
    return render(request,'home.html')

def logout(request):
    auth.logout(request)
    return render(request,'login.html')

#产品管理
def product_manage(request):
    username = request.session.get('user','')
    product_list = Product.objects.all()
    return render(request,'product_manage.html',{'user':username,'products':product_list})

