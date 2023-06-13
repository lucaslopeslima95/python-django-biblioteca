from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import logout,login
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from livro import forms
from django.contrib import messages


def is_logged(request,msg=""):
    return render(request,'listar_livros.html',{'conteudo_pesquisa_form':forms.BuscarLivroForm,'msg':msg})


def login_system(request):
    if request.user.is_authenticated:
        return is_logged(request)
    
    if request.method == "POST":
        form = authForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return is_logged(request)
            else:
                messages.warning(request, "Usuario ou Senha Errados.")
        else:
            messages.warning(request, "Credenciais inválidas.")
    else:
        form = authForm()    
    return render(request, 'login.html', {'form': form})


def salvar_usuario(request):
    if request.method == "POST":
        form = registerForm(request.POST)
        try:
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                email = form.cleaned_data['email']
                
                if User.objects.filter(username=username).exists():
                    messages.warning(request, "Usuario já existe")
                else:
                    User.objects.create_user(username=username, password=password, email=email)
                    messages.success(request, "Salvo com sucesso")
        except Exception as e:
            print(e)
            messages.warning(request, "Ocorreu um erro ao registrar o usuário")
    else:
        form = registerForm()
    return render(request, 'salvar_usuario.html', {'form': form})


def logout_system(request):
    logout(request)
    return redirect('login')

@login_required(login_url="login")
def deletar_usuario(request, id):
    try:
        user = User.objects.get(id=id)
        user.delete()
    except Exception as e:
        print(e)
    return redirect('home')


@login_required(login_url="login")
def atualizar_usuario(request,id):
    obj_user = None
    obj_user = User.objects.get(id=id)
    form = updateForm(request.POST or None, instance=obj_user)
    if request.method == "POST":
        if form.is_valid():
            form.save() 
            messages.success(request, "Atualizado com sucesso")
            return redirect('home')
    return render(request,'atualizar_usuario.html',{'form':form})
    
    
@login_required(login_url="login")
def listar_usuarios(request):
     return render(request,'tables.html',{'users':User.objects.all()})