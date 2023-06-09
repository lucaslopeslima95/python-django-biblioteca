from django.shortcuts import render, redirect
from .forms import RegistroEmprestimoForm
from .models import emprestimo as Emprestimo
from django.http import HttpResponse
from livro.forms import searchBookForm

def listar_emprestimos(request,titulo_livro="titulo_pesquisa"):
    if titulo_livro=="titulo_pesquisa":
        emprestimos = Emprestimo.objects.all()
    else:
        emprestimos = Emprestimo.objects.filter(livro__titulo=titulo_livro)

    return render(request,'listar_emprestimos.html',{'emprestimos':emprestimos, 'conteudo_pesquisa_form':searchBookForm})

def registrar_novo_emprestimo(request):
    if request.method == 'POST':
        form = RegistroEmprestimoForm(request.POST)
        if form.is_valid():
            cliente = form.cleaned_data['cliente']
            livro = form.cleaned_data['livro']
            data_emprestimo = form.cleaned_data['data_emprestimo']
            data_devolucao = form.cleaned_data['data_devolucao']
            
            emprestimo_obj = Emprestimo.objects.create(cliente=cliente, livro=livro, data_emprestimo=data_emprestimo, data_devolucao=data_devolucao)
            emprestimo_obj.save()
            return render(request, 'registro_emprestimo.html', {'form': form})

    else:
        form = RegistroEmprestimoForm()

    return render(request, 'registro_emprestimo.html', {'form': form})

def pesquisar_emprestimo(request):
    titulo = None 
    if request.method == "POST":
        form = searchBookForm(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data.get("titulo")
            
    return listar_emprestimos(request,titulo)

def deletar_emprestimo(request):
    return HttpResponse("deletar emprestimos")