from django.urls import path
from .views import *


app_name = 'emprestimo'

urlpatterns = [
    path('listar_emprestimos/<str:filtro>', listar_emprestimos,name='listar_emprestimos'),
    path('registrar_novo_emprestimo/', registrar_novo_emprestimo,name='registrar_novo_emprestimo'),
    path('pesquisar_emprestimo/', pesquisar_emprestimo,name='pesquisar_emprestimo'),
    path('emprestimo/listar_emprestimos/deletar_emprestimo/<int:id>', deletar_emprestimo,name='deletar_emprestimo'),
    path('encerrar_emprestimo/<int:id>', encerrar_emprestimo,name='encerrar_emprestimo'),
    path('listar_emprestimos/todos_os_emprestimos', listar_emprestimos,name='pos_registro_emprestimo')
]