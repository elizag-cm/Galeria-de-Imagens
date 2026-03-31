from django import forms

from .models import DonoGaleria, Imagem


class ImagemForm(forms.ModelForm):
    class Meta:
        model = Imagem
        fields = ["titulo", "descricao", "arquivo", "categoria", "publicada"]


class DonoGaleriaForm(forms.ModelForm):
    class Meta:
        model = DonoGaleria
        fields = ["nome", "email", "telefone", "instagram", "bio", "foto"]
