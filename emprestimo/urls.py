from django.urls import path
from . import views


app_name = 'emprestimo'

urlpatterns = [
    path('listar_emprestimos/', views.listar_emprestimos,name='listar_emprestimos'),
    path('registrar_novo_emprestimo/', views.registrar_novo_emprestimo,name='registrar_novo_emprestimo'),
    path('pesquisar_emprestimo/', views.pesquisar_emprestimo,name='pesquisar_emprestimo'),
    path('emprestimo/listar_emprestimos/deletar_emprestimo/<int:id>', views.deletar_emprestimo,name='deletar_emprestimo'),
]