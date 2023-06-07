from django.shortcuts import render
from .models import livro
from . import forms

def show_collection(request,msg=""):
    livros = livro.objects.all()
    return render(request,"show_collection.html",{'livros':livros},{'msg',msg})

def register_book_view(request):
    if request.method == "POST":
        form = forms.RegisterBookForm(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data.get("titulo")
            authors = form.cleaned_data.get("authors")
            descricao = form.cleaned_data.get("descricao")
            isbn = form.cleaned_data.get("isbn")
            esta_disponivel = form.cleaned_data.get("esta_disponivel")
            
            try:
                livro_obj = livro.objects.get(titulo=titulo)
                msg = "Livro já existe"
                return show_collection(request, {"msg": msg})
            except livro.DoesNotExist:
                livro_obj = livro.objects.create(titulo=titulo, authors=authors, descricao=descricao, isbn=isbn, esta_disponivel=esta_disponivel)
                msg = "Salvo com sucesso"
                return show_collection(request, {"msg": msg})
    else:
        return show_collection(request)

    
def delete(request, id):
    if request.method == "DELETE":
        try:
            livro_obj = livro.objects.get(id=id)
            livro_obj.delete()
        except livro.DoesNotExist:
            pass
            #return HttpResponse("Livro não encontrado", status=404)
        except Exception as e:
            pass
            #return HttpResponse(f"Erro ao excluir o livro: {str(e)}", status=500)
    else:
        return show_collection(request)

    
def update_user(request):#Terminar o update
    cont = 0
    if request.method == "POST":
        titulo = request.POST.get('titulo')
        livro_novo = livro.objects.filter(titulo=titulo).count()#substituir por get
        if livro_novo>0:
            
            return show_collection(request)
    else:
        return show_collection(request)