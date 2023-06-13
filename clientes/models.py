from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    data_nascimento = models.DateField()
    endereco = models.CharField(max_length=200)
    cpf = models.CharField(max_length=14,unique=True)
    telefone = models.CharField(max_length=30,default=9999-9999)
    pode_fazer_emprestimo = models.BooleanField(default=True)

    def __str__(self):
        return (f"Cliente {self.nome} cpf {self.cpf}")

