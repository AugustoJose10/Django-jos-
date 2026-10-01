from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    data_cadastrio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
