import logging

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.views.decorators.http import require_POST

from .forms import ContactForm

logger = logging.getLogger(__name__)


def contact_page(request):
    return render(request, "contact/page.html", {"form": ContactForm()})


@require_POST
def contact_submit(request):
    form = ContactForm(request.POST)
    if not form.is_valid():
        return render(request, "contact/partials/_contact_form.html", {"form": form})

    contact_message = form.save()

    if settings.CONTACT_RECIPIENTS:
        try:
            send_mail(
                subject=f"Nova mensagem de contato — {contact_message.name}",
                message=(
                    f"Nome: {contact_message.name}\n"
                    f"E-mail: {contact_message.email}\n"
                    f"Telefone: {contact_message.phone}\n\n"
                    f"{contact_message.message}"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=settings.CONTACT_RECIPIENTS,
            )
        except Exception:
            logger.exception("Falha ao enviar e-mail de notificação de contato")

    return render(request, "contact/partials/_contact_success.html")
