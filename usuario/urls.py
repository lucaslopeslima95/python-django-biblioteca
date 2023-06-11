from django.urls import path
from .views import *

urlpatterns = [
    path('', login_system,name='login'),
    path('salvar_usuario',salvar_usuario,name='salvar_usuario'),
    path('home',is_logged,name='home'),
    path('logout', logout_system, name='logout'),
    path('deletar_usuario/<int:id>', deletar_usuario, name='deletar_usuario'),
    path('atualizar_usuario/<int:id>',atualizar_usuario, name='atualizar_usuario'),
]