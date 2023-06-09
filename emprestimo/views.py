from django.shortcuts import render, redirect
from .forms import RegistroEmprestimoForm
from .models import Emprestimo
from livro.models import livro as Livro
from clientes.models import Cliente
from livro.forms import BuscarLivroForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import date

@login_required(login_url="login")
def listar_emprestimos(request,filtro="titulo_pesquisa"):
    try:
        emprestimos = None
        if filtro == "emprestimos_encerrados":
            emprestimos = Emprestimo.objects.filter(status_emprestimo=3)
        elif filtro == "emprestimos_atrasados":
            emprestimos = Emprestimo.objects.filter(status_emprestimo=2)
        elif filtro == "emprestimos_em_dia ":
            emprestimos = Emprestimo.objects.filter(status_emprestimo=1)
        elif filtro == "todos_os_emprestimos":
            emprestimos = Emprestimo.objects.all()
        elif filtro != "titulo_pesquisa" :
            emprestimos = Emprestimo.objects.filter(livro__titulo=filtro)
    except Exception as e:
         print(f" Exceção no Listar emprestimos {e}")

    return render(request,'listar_emprestimos.html',{'emprestimos':emprestimos, 'conteudo_pesquisa_form':BuscarLivroForm})

@login_required(login_url="login")
def registrar_novo_emprestimo(request):
    try:
        if request.method == 'POST':
            form = RegistroEmprestimoForm(request.POST)
            try:
                if form.is_valid():
                        if form.cleaned_data['cliente'].pode_fazer_emprestimo:
                            Cliente.objects.filter(id=form.cleaned_data['cliente'].id).update(pode_fazer_emprestimo = False)
                            Livro.objects.filter(id=form.cleaned_data['livro'].id).update(esta_disponivel = False)
                            form.save()
                        else:
                            messages.warning(request,"Cliente Não pode fazer emprestimos")
            except Exception as e:
                print(f" Exceção no Registrar novo emprestimo {e}")
                
                return redirect('emprestimo:pos_registro_emprestimo')
        else:
         form = RegistroEmprestimoForm()
    except Exception as e:
        print(f"Excecao no registrar novo emprestimo: {e}")

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
                print(f" Exceção no pesquisar emprestimo {e}")
            
    return listar_emprestimos(request,titulo)

@login_required(login_url="login")
def deletar_emprestimo(request,id):
    try:
        Emprestimo.objects.get(id=id).delete()
    except Exception as e:
        print(f" Exceção no deletar emprestimo {e}")

    return redirect('emprestimo:pos_registro_emprestimo')

@login_required(login_url="login")
def encerrar_emprestimo(request,id):
    try:
        emprestimo_encerrado = Emprestimo.objects.get(id=id)
        emprestimo_encerrado.status_emprestimo = 3
        Cliente.objects.filter(id=emprestimo_encerrado.cliente.id).update(pode_fazer_emprestimo = True)
        Livro.objects.filter(id=emprestimo_encerrado.livro.id).update(esta_disponivel=True)
        emprestimo_encerrado.data_conclusao_emprestimo = date.today()
        emprestimo_encerrado.save()
    except Exception as e:
        print(f" Exceção no eencerrar emprestimo {e}")
        
    return redirect('emprestimo:pos_registro_emprestimo')


@login_required(login_url="login")
def atualizar_disponibilidade_livro(id):
    try:
        livro_devolvido = Livro.objects.get(id=id)
        livro_devolvido.esta_disponivel = not livro_devolvido.esta_disponivel
        livro_devolvido.save()
    except Exception as e:
        print(f" Exceção no Atualizar Disponibilidade {e}")

@login_required(login_url="login")
def atualizar_habilitacao_emprestimo_cliente(id):
    try:
        cliente_para_atualizacao = Cliente.objects.get(id=id)
        cliente_para_atualizacao.pode_fazer_emprestimo = not cliente_para_atualizacao.pode_fazer_emprestimo
        cliente_para_atualizacao.save()
    except Exception as e:
        print(f" Exceção no Atualizar Habilitacao Cliente {e}")
