from django.db import models

class Emprestimos(models.Model):
    livro = models.CharField(max_length=200)
    nome_usuario = models.CharField(max_length=100)
    dia_emprestimo = models.IntegerField()
    dia_devolucao = models.CharField(max_length=100)

    def __str__(self):
        return self.livro
