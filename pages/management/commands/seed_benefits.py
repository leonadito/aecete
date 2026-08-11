from django.core.management.base import BaseCommand

from pages.models import Benefit
from pages.seed_utils import attach_image

BENEFITS = [
    (
        "Descontos em Comércios",
        "discount",
        "descontos.png",
        "AICITI junto com o comércio local irá disponibilizar descontos para "
        "associados. Em breve você terá a lista dos locais com desconto para você.",
    ),
    (
        "Site e CRM",
        "crm",
        "crm.png",
        "Além do site e CRM, a AICITI irá publicar semanalmente notícias sobre o "
        "litoral norte gaúcho e o mercado imobiliário.",
    ),
    (
        "Anúncios e Divulgações",
        "megaphone",
        "anuncios.png",
        "A AICITI terá o prazer de divulgar suas imobiliárias parceiras e "
        "compartilhar as publicações dos associados, ampliando ainda mais sua "
        "visibilidade.",
    ),
]


class Command(BaseCommand):
    help = "Semeia os 3 benefícios para associados (conteúdo real migrado do site atual)."

    def handle(self, *args, **options):
        created = 0
        for order, (title, icon, image, description) in enumerate(BENEFITS, start=1):
            benefit, was_created = Benefit.objects.update_or_create(
                title=title,
                defaults={"icon": icon, "description": description, "order": order},
            )
            attach_image(benefit, "image", "benefits", image)
            created += was_created

        self.stdout.write(self.style.SUCCESS(f"Benefícios semeados ({created} novos registros)."))
