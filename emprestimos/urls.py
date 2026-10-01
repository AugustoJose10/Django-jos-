from django.urls import path
from . import views


urlpatterns = [
    path('', views.lista_emprestimos, name='lista_emprestimos'),
]