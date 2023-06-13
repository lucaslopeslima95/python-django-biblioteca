from django.db import models

class livro(models.Model):
    titulo = models.CharField(max_length=30)
    autor = models.CharField(max_length=30)
    descricao = models.CharField(max_length=200)
    isbn = models.CharField(max_length=20,unique=True)
    esta_disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo
