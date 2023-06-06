from django.shortcuts import render
from .models import livro
from . import forms

def show_colletion(request):
    livros = livro.objects.all()
    return render(request,"show_collection.html",{'livros':livros})

def register_book(request):
    if request.method == "POST":
        form = forms.registerBookForm(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data.get("titulo")
            authors = form.cleaned_data.get("authors")
            descricao = form.cleaned_data.get("descricao")
            isbn = form.cleaned_data.get("isbn")
            esta_disponivel = form.cleaned_data.get("esta_disponivel")
            livro_novo = livro.objects.filter(titulo=titulo).count()#substituir por get
            if livro_novo>0:
                msg = "Livro ja Existe"
                return render(request, "register.html", {"form": form, "msg": msg})
            else:
                livro = livro.objects.create_user(titulo=titulo,authors=authors,descricao=descricao,isbn=isbn,esta_disponivel=esta_disponivel)
                livro.save()
                return show_colletion(request)
    else:
        return show_colletion(request)
    
def delete(request,id):
    if request == "DELETE":    
        try:
            livro.objects.get(id=id).delete()
        except Exception as e: 
            print(e)
            
    return  show_colletion(request)
    
def update_user(request):#Terminar o update
    cont = 0
    if request.method == "POST":
        titulo = request.POST.get('titulo')
        livro_novo = livro.objects.filter(titulo=titulo).count()#substituir por get
        if livro_novo>0:
            
            return show_colletion(request)
    else:
        return show_colletion(request)