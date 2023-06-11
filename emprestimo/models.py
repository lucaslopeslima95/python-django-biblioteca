from django.db import models
from livro.models import livro
from clientes.models import Cliente

class Status_emprestimo(models.IntegerChoices):
        EM_DIA = 1,
        ATRASADO = 2,
        CONCLUIDO = 3
        
class Emprestimo(models.Model):
    
    livro = models.ForeignKey(livro, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_emprestimo = models.DateField()
    data_devolucao = models.DateField()
    status_emprestimo = models.IntegerField(default=Status_emprestimo.EM_DIA ,choices=Status_emprestimo.choices)

    def __str__(self):
        return f"Empréstimo de {self.livro} para {self.cliente}"



   