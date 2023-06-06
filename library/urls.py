from django.contrib import admin
from django.urls import path,include
from usuario import urls as usuario
from livro import urls as livros


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(usuario)),
    path('livros/',include(livros, namespace="livros"))
]
