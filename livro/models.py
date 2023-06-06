from django.db import models

class livro(models.Model):
    titulo = models.CharField(max_length=30)
    authors = models.CharField(max_length=30)
    descricao = models.CharField(max_length=200)
    isbn = models.CharField(max_length=31)
    esta_disponivel = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
