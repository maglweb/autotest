from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate,login

# Create your views here.
#def test(request):
 #   return HttpResponse('hello test')

def login(request):
    return render(request,'login.html')