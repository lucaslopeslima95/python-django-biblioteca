from django.db import models
from livro.models import livro
from clientes.models import Cliente

class emprestimo(models.Model):
    livro = models.ForeignKey(livro, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_emprestimo = models.DateField()
    data_devolucao = models.DateField()
    situacao = models.BooleanField(default=False)
    # Outros campos do empréstimo

    def __str__(self):
        return f"Empréstimo de {self.livro} para {self.cliente}"




   