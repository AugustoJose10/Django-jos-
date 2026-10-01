from django.shortcuts import render

from .models import Usuario


def lista_usuarios(request):
    # BACK: busca todos os usuarios no banco
    usuarios = Usuario.objects.all()

    # VIEW -> FRONT: manda a lista para usuarios.html
    return render(request, 'usuarios.html', {'usuarios': usuarios})