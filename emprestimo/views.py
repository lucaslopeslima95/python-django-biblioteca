from django.shortcuts import render, redirect
from .forms import RegistroEmprestimoForm
from .models import Emprestimo
from django.http import HttpResponse
from livro.forms import BuscarLivroForm

def listar_emprestimos(request,titulo_livro="titulo_pesquisa"):
    if titulo_livro=="titulo_pesquisa":
        emprestimos = Emprestimo.objects.all()
    else:
        emprestimos = Emprestimo.objects.filter(livro__titulo=titulo_livro)

    return render(request,'listar_emprestimos.html',{'emprestimos':emprestimos, 'conteudo_pesquisa_form':BuscarLivroForm})

def registrar_novo_emprestimo(request):
    if request.method == 'POST':
        form = RegistroEmprestimoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except Exception as e:
                print(e)
            return redirect('emprestimo:listar_emprestimos')
    else:
        form = RegistroEmprestimoForm()

    return render(request, 'registro_emprestimo.html', {'form': form})

def pesquisar_emprestimo(request):
    titulo = None 
    if request.method == "POST":
        form = BuscarLivroForm(request.POST)
        if form.is_valid():
            try:
             titulo = form.cleaned_data.get("titulo")
            except Exception as e:
                print(e)
            
    return listar_emprestimos(request,titulo)

def deletar_emprestimo(request,id):
    try:
        Emprestimo.objects.get(id=id).delete()
    except Exception as e:
        print(e)

    return redirect('emprestimo:listar_emprestimos')


def encerrar_emprestimo(request,id):
    try:
        emprestimo_encerrado = Emprestimo.objects.get(id=id)
        emprestimo_encerrado.status_emprestimo = 3
        emprestimo_encerrado.save()
    except Exception as e:
        print(e)
    return redirect('emprestimo:listar_emprestimos')