from django.urls import path
from . import views


app_name = 'clientes'

urlpatterns = [
    path('listar_clientes/', views.listar_clientes,name='listar_clientes'),
    path('registrar_novo_cliente/', views.registrar_novo_cliente,name='registrar_novo_cliente'),
    path('pesquisar_cliente/', views.pesquisar_cliente,name='pesquisar_cliente'),
    path('listar_clientes/deletar_cliente/<int:id>', views.deletar_cliente,name='deletar_cliente'),
]