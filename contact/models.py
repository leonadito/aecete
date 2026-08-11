from django.db import models


class ContactMessage(models.Model):
    name = models.CharField("nome", max_length=150)
    email = models.EmailField("e-mail")
    phone = models.CharField("telefone", max_length=30, blank=True)
    message = models.TextField("mensagem")
    created_at = models.DateTimeField("criado em", auto_now_add=True)
    is_reviewed = models.BooleanField("revisado", default=False)

    class Meta:
        verbose_name = "mensagem de contato"
        verbose_name_plural = "mensagens de contato"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} <{self.email}> — {self.created_at:%d/%m/%Y %H:%M}"
