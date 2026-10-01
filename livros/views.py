from django.shortcuts import render

from .models import Livros


def lista_livros(request):
    # 1. O BACK busca os dados no banco de dados
    livros = Livros.objects.all()

    # 2. A VIEW entrega os dados para o FRONT (template)
    #    'livros.html' e o dicionario {'livros': livros}
    #    dentro do HTML o nome "livros" vira a variavel usada no {% for %}
    return render(request, 'livros.html', {'livros': livros})