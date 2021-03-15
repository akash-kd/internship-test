from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import CreateUser
from django.contrib.auth import authenticate,login as dj_login,logout as dj_logout
# Create your views here.
from main.models import tracker

def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            dj_login(request, user)
            return redirect('/')
        else:
            return render(request,'accounts/login.html',{'error':True})
    return render(request,'accounts/login.html')

def regis(request):
    form = CreateUser()

    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    data = {
        'form':form
    }   
    return render(request,'accounts/regis.html',data)

def logout(request):
    dj_logout(request)
    return redirect('/')
