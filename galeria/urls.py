from django.urls import path

from . import views

urlpatterns = [
    path("", views.lista_galeria, name="lista_galeria"),
    path("adicionar/", views.adicionar_imagem, name="adicionar_imagem"),
    path("dono/", views.editar_dono, name="editar_dono"),
]
