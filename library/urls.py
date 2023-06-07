from django.contrib import admin
from django.urls import path, include
from usuario import urls as usuario_urls
from livro import urls as livros_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(usuario_urls)),
    path('livros/', include(livros_urls, namespace="livros")),
]
