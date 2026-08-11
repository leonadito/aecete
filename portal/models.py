from django.conf import settings
from django.db import models


class Builder(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        verbose_name="usuário",
        on_delete=models.CASCADE,
        related_name="builder",
    )
    name = models.CharField("nome da construtora", max_length=150)
    logo = models.ImageField("logo", upload_to="builders/", blank=True, null=True)
    is_active = models.BooleanField("ativo", default=True)
    created_at = models.DateTimeField("criado em", auto_now_add=True)

    class Meta:
        verbose_name = "construtora"
        verbose_name_plural = "construtoras"
        ordering = ["name"]

    def __str__(self):
        return self.name


class PriceTable(models.Model):
    builder = models.ForeignKey(
        Builder,
        verbose_name="construtora",
        on_delete=models.CASCADE,
        related_name="price_tables",
    )
    title = models.CharField("nome da tabela", max_length=200)
    description = models.TextField("descrição")
    image = models.ImageField("imagem", upload_to="price_tables/")
    drive_link = models.URLField("link do drive")
    is_active = models.BooleanField("ativo", default=True)
    created_at = models.DateTimeField("criado em", auto_now_add=True)
    updated_at = models.DateTimeField("atualizado em", auto_now=True)

    class Meta:
        verbose_name = "tabela de preços"
        verbose_name_plural = "tabelas de preços"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.title} — {self.builder.name}"
