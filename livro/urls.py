from django.urls import path
from . import views


app_name = 'livros'

urlpatterns = [
    path('show_collection/', views.show_collection,name='show_collection'),
    path('register_book/', views.register_book,name='register_book'),
    path('pesquisar_livro/', views.pesquisar_livro,name='pesquisar_livro'),
    path('show_collection/delete/<int:id>', views.delete,name='delete'),
]