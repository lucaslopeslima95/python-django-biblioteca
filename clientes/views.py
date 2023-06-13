from django.shortcuts import render, redirect
from .models import Cliente
from . import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from emprestimo.models import Emprestimo
from django.contrib import messages

@login_required(login_url="login")
def listar_clientes(request,aviso_ao_usuario="",nome_cliente="listar_todos"):
    
    clientes=None
    try:
        if nome_cliente == "listar_todos":
            clientes = Cliente.objects.all()
        else:
            clientes = Cliente.objects.filter(nome__startswith=nome_cliente)
    except Exception as e:
        print(f" excecao no listar clientes {e}")

    nome_cliente_para_filtrar = forms.BuscaClienteNomeForm()

    return render(request,"listar_clientes.html",{'clientes':clientes ,'nome_cliente_para_filtrar':nome_cliente_para_filtrar})

@login_required(login_url="login")
def registrar_novo_cliente(request):
    if request.method == "POST":
        form_cliente = forms.ClienteForm(request.POST)
        if form_cliente.is_valid():
            try:
                obj_cliente = form_cliente.save(commit=False)
                if Cliente.objects.filter(email=obj_cliente.email).exists() \
                and Cliente.objects.filter(cpf=obj_cliente.email).exists():
                    aviso_ao_usuario = "Email já ou Cpf já cadastrado"
                    return listar_clientes(request, aviso_ao_usuario=aviso_ao_usuario)
                else:
                    obj_cliente.save()
                    aviso_ao_usuario = "Cliente Salvo Com Sucesso"
                    return redirect('clientes:listar_clientes')
            except Exception as e:
                print(f" excecao no registrar novo cliente {e}")
    else:
        form_cliente = forms.ClienteForm() 
    return render(request, 'registrar_novo_cliente.html', {'form_cliente': form_cliente})

 
@login_required(login_url="login")  
def deletar_cliente(request, id):
    if request.method == "GET":
        try:
            obj_cliente = Cliente.objects.get(id=id)
            if obj_cliente.pode_fazer_emprestimo:
                obj_cliente.delete()
                messages.success(request, "Apagado com sucesso.")
            else:
                messages.warning(request, "Não é possivel apagar clientes com débitos.")
            
        except Exception as e:
            print(f"Excecao no deletar cliente {e}")
           
    return listar_clientes(request)
    

@login_required(login_url="login")   
def atualizar_cliente(request,id):
    cliente = None
    if request.method == "POST":
        try:
            cliente = Cliente.objects.get(id=id)
            form = forms.ClienteForm(request.POST or None, instance=cliente)
            if form.is_valid():
                form.save() 
                return redirect('clientes:listar_clientes')
        except Exception as e:
            print(f"Excecao no atualizar cliente {e}")
            
    else:
         return render(request,'atualizar_cliente.html',{'form':form})  
        
@login_required(login_url="login") 
def pesquisar_cliente(request):
    nome_cliente = None
    try:
        if request.method == "POST":
            form_busca_cliente_nome = forms.BuscaClienteNomeForm(request.POST)
            if form_busca_cliente_nome.is_valid():
                nome_cliente = form_busca_cliente_nome.cleaned_data.get("nome_cliente")
                print(nome_cliente)
    except Exception as e:
        print(f"Excecao no pesquisar cliente {e}")
    return listar_clientes(request,nome_cliente=nome_cliente)
