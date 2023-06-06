from django.urls import path
from . import views


app_name = 'livros'

urlpatterns = [
    path('show_collection/', views.show_colletion,name='show_collection'),
    path('register_book/', views.register_book,name='register_book'),
]