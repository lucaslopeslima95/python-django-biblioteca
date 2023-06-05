from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import logout,login
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

def login_sistem(request):
    if request.method == "POST":
              form = authForm(request.POST)
              if form.is_valid():
                     username = form.cleaned_data['username']
                     password = form.cleaned_data['password']
                     user = authenticate(username=username, password=password)
                     if user:
                            login(request,user)
                            return home(request)
                           
                     else:
                            return HttpResponse('Email ou senha Invalido')
    else:
        form = authForm()
            
    return render(request,'login.html',{'form':form})


def register(request=""):
    msg = None
    success = False

    if request.method == "POST":
        form = registerForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = User.objects.filter(username=username).first()
            if user:
                msg = "Usuario ja Existe"
                return render(request, "register.html", {"form": form, "msg": msg, "success": success})
            else:
                user = User.objects.create_user(username=username,password=password)
                user.save()
                msg = "Salvo com sucesso"
                form = authForm()
                return render(request,'login.html',{'form':form})
    else:
        form = registerForm()

    return render(request,'register.html',{'form':form})
    
@login_required(login_url="home")
def home(request):
    users =  User.objects.all()
    return render(request,'tables.html',{'users':users})


def logout_sis(request):
    logout(request)
    return redirect('login')  

def delete(number_row):
    pass
