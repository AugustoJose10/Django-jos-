from django.db import models

class Livros(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    ano_publicacao = models.IntegerField()
    editora = models.CharField(max_length=100)
    quantidade_disponivel = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo
