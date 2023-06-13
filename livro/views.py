from django.shortcuts import render,redirect
from .models import livro as Livro
from . import forms
from django.contrib.auth.decorators import login_required

@login_required(login_url="login")
def listar_livros(request,msg="",titulo_livro="sem_pesquisa"):
    if titulo_livro == "sem_pesquisa":
        livros = Livro.objects.all()
    else:
        livros = Livro.objects.filter(titulo__startswith=titulo_livro)
    conteudo_pesquisa_form = forms.BuscarLivroForm()
    return render(request,"listar_livros.html",{'livros':livros ,'msg':msg,'conteudo_pesquisa_form':conteudo_pesquisa_form})

@login_required(login_url="login")
def registrar_livro(request):
    if request.method == "POST":
        form = forms.LivroForm(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data.get("titulo")
            autor = form.cleaned_data.get("autor")
            descricao = form.cleaned_data.get("descricao")
            isbn = form.cleaned_data.get("isbn")
            esta_disponivel = True
            livro_obj = None
            try:
                livro_obj = Livro.objects.get(titulo=titulo)    
            except Exception as e:
                print(e)
                
            if livro_obj:
                msg = "Livro já existe"
                return listar_livros(request, {"msg": msg})
            else:
                livro_obj = Livro.objects.create(titulo=titulo, autor=autor, descricao=descricao, isbn=isbn, esta_disponivel=esta_disponivel)
                msg = "Salvo com sucesso"
            return listar_livros(request, {"msg": msg})
    else:
        form = forms.LivroForm()
    return render(request,'registrar_livro.html',{'form':form})
    
@login_required(login_url="login") 
def apagar_livro(request, id):
    if request.method == "GET":
        try:
            livro_obj = Livro.objects.get(id=id)
            livro_obj.delete()
        except Exception as e:
            print(e)
        return listar_livros(request)
    else:
        return listar_livros(request)

    
@login_required(login_url="login")
def atualizar_livro(request,id):
    obj_livro = None
    obj_livro = Livro.objects.get(id=id)
    form = forms.LivroForm(request.POST or None, instance=obj_livro)
    if request.method == "POST":
        if form.is_valid():
            form.save() 
            return redirect('livros:listar_livros')
    return render(request,'atualizar_livro.html',{'form':form})
    
    
@login_required(login_url="login")
def pesquisar_livro(request):
    if request.method == "POST":
        form = forms.BuscarLivroForm(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data.get("titulo")
            
    return listar_livros(request,titulo_livro=titulo)
    