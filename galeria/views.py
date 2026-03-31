from django.shortcuts import redirect, render

from .forms import DonoGaleriaForm, ImagemForm
from .models import Categoria, DonoGaleria, Imagem


def lista_galeria(request):
    categoria_slug = request.GET.get("categoria")
    categorias = Categoria.objects.filter(ativa=True)
    imagens = Imagem.objects.filter(publicada=True).select_related("categoria")

    if categoria_slug:
        imagens = imagens.filter(categoria__slug=categoria_slug)

    context = {
        "imagens": imagens,
        "categorias": categorias,
        "categoria_ativa": categoria_slug,
        "dono": DonoGaleria.objects.first(),
    }
    return render(request, "galeria/lista_galeria.html", context)


def adicionar_imagem(request):
    if request.method == "POST":
        form = ImagemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("lista_galeria")
    else:
        form = ImagemForm()

    return render(request, "galeria/adicionar_imagem.html", {"form": form})


def editar_dono(request):
    dono = DonoGaleria.objects.first()

    if request.method == "POST":
        form = DonoGaleriaForm(request.POST, request.FILES, instance=dono)
        if form.is_valid():
            form.save()
            return redirect("lista_galeria")
    else:
        form = DonoGaleriaForm(instance=dono)

    return render(request, "galeria/editar_dono.html", {"form": form, "dono": dono})
