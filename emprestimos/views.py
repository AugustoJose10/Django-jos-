from django.shortcuts import render

from .models import Emprestimos


def lista_emprestimos(request):
    # BACK: busca todos os emprestimos no banco
    emprestimos = Emprestimos.objects.all()

    # VIEW -> FRONT: manda a lista para emprestimos.html
    return render(request, 'emprestimos.html', {'emprestimos': emprestimos})