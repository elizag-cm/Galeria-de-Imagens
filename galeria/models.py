from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True)
    ativa = models.BooleanField(default=True)
    criada_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ["nome"]

    def __str__(self):
        return self.nome


class Imagem(models.Model):
    titulo = models.CharField(max_length=150)
    descricao = models.TextField(blank=True)
    arquivo = models.ImageField(upload_to="galeria/")
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name="imagens",
    )
    publicada = models.BooleanField(default=True)
    criada_em = models.DateTimeField(auto_now_add=True)
    atualizada_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Imagem"
        verbose_name_plural = "Imagens"
        ordering = ["-criada_em"]

    def __str__(self):
        return self.titulo
