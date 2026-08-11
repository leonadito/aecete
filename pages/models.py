from django.db import models


class BoardMember(models.Model):
    class Group(models.TextChoices):
        DIRETORIA = "DIRETORIA", "Diretoria"
        TITULAR = "TITULAR", "Membro titular"
        SUPLENTE = "SUPLENTE", "Membro suplente"

    name = models.CharField("nome", max_length=150)
    role = models.CharField("cargo", max_length=100, blank=True)
    group = models.CharField(
        "grupo", max_length=20, choices=Group.choices, default=Group.TITULAR
    )
    photo = models.ImageField("foto", upload_to="board/", blank=True, null=True)
    order = models.PositiveIntegerField("ordem", default=0)

    class Meta:
        verbose_name = "integrante da diretoria"
        verbose_name_plural = "integrantes da diretoria"
        ordering = ["group", "order", "name"]

    def __str__(self):
        return f"{self.name} ({self.role})" if self.role else self.name


class Benefit(models.Model):
    title = models.CharField("título", max_length=150)
    icon = models.CharField(
        "ícone",
        max_length=50,
        help_text="Chave simbólica do ícone de fallback (ex: discount, crm, megaphone).",
    )
    image = models.ImageField("imagem", upload_to="benefits/", blank=True, null=True)
    description = models.TextField("descrição")
    order = models.PositiveIntegerField("ordem", default=0)

    class Meta:
        verbose_name = "benefício"
        verbose_name_plural = "benefícios"
        ordering = ["order", "id"]

    def __str__(self):
        return self.title


class FAQItem(models.Model):
    question = models.CharField("pergunta", max_length=255)
    answer = models.TextField("resposta")
    order = models.PositiveIntegerField("ordem", default=0)

    class Meta:
        verbose_name = "pergunta frequente"
        verbose_name_plural = "perguntas frequentes"
        ordering = ["order", "id"]

    def __str__(self):
        return self.question
