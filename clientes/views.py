from django.shortcuts import render, redirect
from .models import Cliente
from . import forms
from django.contrib import messages


def listar_clientes(request,aviso_ao_usuario="",nome_cliente="listar_todos"):
    messages.error(request,aviso_ao_usuario)
    clientes=None
    try:
        if nome_cliente == "listar_todos":
            clientes = Cliente.objects.all()
        else:
            clientes = Cliente.objects.filter(nome__startswith=nome_cliente)
    except Exception as e:
        print(e)

    nome_cliente_para_filtrar = forms.BuscaClienteNomeForm()

    return render(request,"listar_clientes.html",{'clientes':clientes ,'messages':messages,'nome_cliente_para_filtrar':nome_cliente_para_filtrar})

def registrar_novo_cliente(request):
    if request.method == "POST":
        form_cliente = forms.ClienteForm(request.POST)
        if form_cliente.is_valid():
            try:
                obj_cliente = form_cliente.save(commit=False)
                if Cliente.objects.filter(email=obj_cliente.email).exists():
                    aviso_ao_usuario = "Email já ou Cliente já cadastrado"
                    return listar_clientes(request, aviso_ao_usuario=aviso_ao_usuario)
                else:
                    obj_cliente.save()
                    aviso_ao_usuario = "Cliente Salvo Com Sucesso"
                    return redirect('clientes:listar_clientes')
            except Exception as e:
                print(e)
    else:
        form_cliente = forms.ClienteForm() 
    return render(request, 'registrar_novo_cliente.html', {'form_cliente': form_cliente})

   
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

    
def atualizar_cliente(request,id):
    cliente = None
    cliente = Cliente.objects.get(id=id)
    form = forms.ClienteForm(request.POST or None, instance=cliente)
    if request.method == "POST":
        if form.is_valid():
            form.save() 
            return redirect('clientes:listar_clientes')
    else:
         return render(request,'atualizar_cliente.html',{'form':form})  
        
    
def pesquisar_cliente(request):
    nome_cliente = None
    if request.method == "POST":
        form_busca_cliente_nome = forms.BuscaClienteNomeForm(request.POST)
        if form_busca_cliente_nome.is_valid():
            nome_cliente = form_busca_cliente_nome.cleaned_data.get("nome_cliente")
            print(nome_cliente)
    return listar_clientes(request,nome_cliente=nome_cliente)
