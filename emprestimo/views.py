from django.shortcuts import render, redirect
from django.shortcuts import  reverse
from .forms import RegistroEmprestimoForm
from .models import Emprestimo
from livro.models import livro as Livro
from livro.forms import BuscarLivroForm
from django.contrib.auth.decorators import login_required

@login_required(login_url="login")
def listar_emprestimos(request,filtro="titulo_pesquisa"):
    emprestimos = None
    if filtro == "emprestimos_encerrados":
        emprestimos = Emprestimo.objects.filter(status_emprestimo=3)
    elif filtro == "emprestimos_atrasados":
        emprestimos = Emprestimo.objects.filter(status_emprestimo=2)
    elif filtro == "emprestimos_em_dia":
        emprestimos = Emprestimo.objects.filter(status_emprestimo=1)
    elif filtro == "todos_os_emprestimos":
        emprestimos = Emprestimo.objects.all()
    elif filtro != "titulo_pesquisa" :
        emprestimos = Emprestimo.objects.filter(livro__titulo=filtro)

    return render(request,'listar_emprestimos.html',{'emprestimos':emprestimos, 'conteudo_pesquisa_form':BuscarLivroForm})

@login_required(login_url="login")
def registrar_novo_emprestimo(request):
    if request.method == 'POST':
        form = RegistroEmprestimoForm(request.POST)
        if form.is_valid():
            try:
                atualizar_disponibilidade_livro(form.cleaned_data['livro'].id)
                form.save()
            except Exception as e:
                print(e)
            
            return redirect('login')
    else:
        form = RegistroEmprestimoForm()

    return render(request, 'registro_emprestimo.html', {'form': form})

@login_required(login_url="login")
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

@login_required(login_url="login")
def deletar_emprestimo(request,id):
    try:
        Emprestimo.objects.get(id=id).delete()
    except Exception as e:
        print(e)

    return redirect('emprestimo:listar_emprestimos')

@login_required(login_url="login")
def encerrar_emprestimo(request,id):
    try:
        emprestimo_encerrado = Emprestimo.objects.get(id=id)
        emprestimo_encerrado.status_emprestimo = 3
        atualizar_disponibilidade_livro(emprestimo_encerrado.livro.id)
        emprestimo_encerrado.save()
    except Exception as e:
        print(e)
    return redirect('login')

@login_required(login_url="login")
def atualizar_disponibilidade_livro(id):
    livro_devolvido = Livro.objects.get(id=id)
    livro_devolvido.esta_disponivel = not livro_devolvido.esta_disponivel
    livro_devolvido.save()