from django.urls import path
from . import views


app_name = 'livros'

urlpatterns = [
    path('listar_livros/', views.listar_livros,name='listar_livros'),
    path('registrar_livro/', views.registrar_livro,name='registrar_livro'),
    path('pesquisar_livro/', views.pesquisar_livro,name='pesquisar_livro'),
    path('listar_livros/apagar_livro/<int:id>', views.apagar_livro,name='apagar_livro'),
    path('atualizar_livro/<int:id>', views.atualizar_livro,name='atualizar_livro'),
]