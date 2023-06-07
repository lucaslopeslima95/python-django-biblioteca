from django.contrib import admin
from django.urls import path, include
from usuario import urls as usuario_urls
from livro import urls as livros_urls
from clientes import urls as cliente_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(usuario_urls)),
    path('livros/', include(livros_urls, namespace="livros")),
    path('cliente/', include(cliente_urls, namespace="cliente")),   
]
