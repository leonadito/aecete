from django.db import models


class Partner(models.Model):
    class Kind(models.TextChoices):
        PARTNER = "PARTNER", "Parceiro comercial"
        MEMBER_AGENCY = "MEMBER_AGENCY", "Imobiliária associada"

    name = models.CharField("nome", max_length=150)
    kind = models.CharField(
        "tipo", max_length=20, choices=Kind.choices, default=Kind.PARTNER
    )
    logo = models.ImageField("logo", upload_to="partners/", blank=True, null=True)
    website_url = models.URLField("site", blank=True)
    facebook_url = models.URLField("facebook", blank=True)
    instagram_url = models.URLField("instagram", blank=True)
    order = models.PositiveIntegerField("ordem", default=0)
    is_active = models.BooleanField("ativo", default=True)

    class Meta:
        verbose_name = "parceiro"
        verbose_name_plural = "parceiros"
        ordering = ["order", "name"]

    def __str__(self):
        return self.name
