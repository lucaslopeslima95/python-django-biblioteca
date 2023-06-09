from django.shortcuts import render
from .models import livro
from . import forms

def show_collection(request,msg="",titulo_livro="sem_pesquisa"):
    if titulo_livro == "sem_pesquisa":
        livros = livro.objects.all()
    else:
        livros = livro.objects.filter(titulo__startswith=titulo_livro)
    conteudo_pesquisa_form = forms.searchBookForm()
    return render(request,"show_collection.html",{'livros':livros ,'msg':msg,'conteudo_pesquisa_form':conteudo_pesquisa_form})

def register_book(request):
    if request.method == "POST":
        form = forms.registerBookForm(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data.get("titulo")
            authors = form.cleaned_data.get("authors")
            descricao = form.cleaned_data.get("descricao")
            isbn = form.cleaned_data.get("isbn")
            esta_disponivel = True
            livro_obj = ""
            try:
                livro_obj = livro.objects.get(titulo=titulo)    
            except Exception as e:
                print(e)
                
            if livro_obj:
                msg = "Livro já existe"
                return show_collection(request, {"msg": msg})
            else:
                livro_obj = livro.objects.create(titulo=titulo, authors=authors, descricao=descricao, isbn=isbn, esta_disponivel=esta_disponivel)
                msg = "Salvo com sucesso"
            return show_collection(request, {"msg": msg})
    else:
        form = forms.registerBookForm()
        return render(request,'register_book.html',{'form':form})
    
def delete(request, id):
    if request.method == "GET":
        try:
            livro_obj = livro.objects.get(id=id)
            livro_obj.delete()
        except Exception as e:
            print(e)
        return show_collection(request)
    else:
        return show_collection(request)

    
def update_book(request):#Terminar o update
    cont = 0
    if request.method == "POST":
        titulo = request.POST.get('titulo')
        livro_novo = livro.objects.filter(titulo=titulo).count()#substituir por get
        if livro_novo>0:
            
         return show_collection(request)
    else:
        return show_collection(request)
    
    
def pesquisar_livro(request):
    if request.method == "POST":
        form = forms.searchBookForm(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data.get("titulo")
            
    return show_collection(request,titulo_livro=titulo)
    