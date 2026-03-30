from django.contrib import admin
from .models import Categoria, Imagem


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome", "ativa", "criada_em")
    list_filter = ("ativa",)
    search_fields = ("nome", "slug")
    prepopulated_fields = {"slug": ("nome",)}


@admin.register(Imagem)
class ImagemAdmin(admin.ModelAdmin):
    list_display = ("titulo", "categoria", "publicada", "criada_em")
    list_filter = ("publicada", "categoria")
    search_fields = ("titulo", "descricao")
