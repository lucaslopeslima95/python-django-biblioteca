from django.shortcuts import render, redirect
from .models import Cliente
from . import forms

def listar_clientes(request,aviso_ao_usuario="",nome_cliente="listar_todos"):
    try:
        if nome_cliente == "listar_todos":
            clientes = Cliente.objects.all()
        else:
            clientes = Cliente.objects.filter(nome__startswith=nome_cliente)
    except Exception as e:
        print(e)

    nome_cliente_para_filtrar = forms.BuscaClienteNomeForm()

    return render(request,"listar_clientes.html",{'clientes':clientes ,'aviso_ao_usuario':aviso_ao_usuario,'nome_cliente_para_filtrar':nome_cliente_para_filtrar})

def registrar_novo_cliente(request):
    if request.method == "POST":
        form_cliente = forms.ClienteForm(request.POST)
        if form_cliente.is_valid():
            try:
                obj_cliente = form_cliente.save(commit=False)
                if Cliente.objects.filter(email=obj_cliente.email).exists():
                    aviso_ao_usuario = "Email já ou Cliente já cadatrado"
                    return listar_clientes(request,aviso_ao_usuario)   
                else:
                    obj_cliente.save()
                    aviso_ao_usuario = "Cliente Salvo Com Sucesso"
                    return listar_clientes(request,aviso_ao_usuario)
            except Exception as e:
                print(e)
    else:
        return listar_clientes(request)

   
def deletar_cliente(request, id):
    if request.method == "GET":
        try:
            obj_cliente = Cliente.objects.get(id=id)
            obj_cliente.delete()
            aviso_ao_usuario = "Cliente Deletado Com Sucesso"
        except Exception as e:
            aviso_ao_usuario = "Não foi Possivel deletar o cliente"
            print(e)
        return listar_clientes(request,aviso_ao_usuario=aviso_ao_usuario)
    else:
        return listar_clientes(request,aviso_ao_usuario=aviso_ao_usuario)

    
def atualizar_cliente(request):#Terminar o update
    if request.method == "POST":
        nome_cliente = request.POST.get('nome_cliente')
        livro_novo = Cliente.objects.filter(nome_cliente=nome_cliente).count()#substituir por get
        if livro_novo>0:
            
         return listar_clientes(request)
    else:
        return listar_clientes(request)
    
    
def pesquisar_cliente(request):
    if request.method == "POST":
        form_busca_cliente_nome = forms.BuscaClienteNomeForm(request.POST)
        if form_busca_cliente_nome.is_valid():
            nome_cliente = form_busca_cliente_nome.cleaned_data.get("nome")
            listar_clientes(request,nome_cliente=nome_cliente)
    