from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import logout,login
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

def login_sistem(request):

    if request.user.is_authenticated:
         updateForm = update_User_Form()
         return render(request,'tables.html',{'users':User.objects.all(),'form':updateForm})
    
    elif request.method == "POST":
              form = authForm(request.POST)
              if form.is_valid():
                     username = form.cleaned_data['username']
                     password = form.cleaned_data['password']
                     user = authenticate(username=username, password=password)
                     if user is not None:
                            login(request,user)
                            updateForm = update_User_Form()
                            return render(request,'tables.html',{'users':User.objects.all(),'form':updateForm})
    else:
        form = authForm()    
        return render(request,'login.html',{'form':form})


def register_user(request):
    msg = None
    if request.method == "POST":
        form = registerForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            email = form.cleaned_data.get("email")
            user = User.objects.filter(username=username).first()#substituir por get
            if user:
                msg = "Usuario ja Existe"
                return render(request, "register.html", {"form": form, "msg": msg})
            else:
                user = User.objects.create_user(username=username,password=password,email=email)
                user.save()
                msg = "Salvo com sucesso"
                form = authForm()
                return render(request,'login.html',{'form':form})
    else:
        form = registerForm()
        return render(request,'register.html',{'form':form})
    
@login_required(login_url="login")
def to_home_page(request=""):
    users =  User.objects.all()
    return render(request,'tables.html',{'users':users})


def logout_sistem(request):
    logout(request)
    form = authForm()
    return render(request,'login.html',{'form':form})

def delete(request,id):
    User.objects.get(id=id).delete()
    users =  User.objects.all()
    return render(request,'tables.html',{'users':users})


@login_required
def update_user(request):
    cont = 0
    if request.method == "POST":
        username = request.POST.get('username')
        cont = User.objects.filter(username=username).count()
        if cont>0:
            user = User.objects.get('username')
            user.email = request.POST.get('email')
            user.set_password(request.POST.get('password'))
            user.save()
            users = User.objects.all()
            return render(request, 'tables.html', {'users': users})
    else:
        users = User.objects.all()
        return render(request, 'tables.html', {'users': users})
