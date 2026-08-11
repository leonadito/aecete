from django.core.management.base import BaseCommand

from pages.seed_utils import attach_image
from partners.models import Partner

PARTNERS = [
    ("Academia UP", "academia-up.jpg"),
    ("Panela Food Burger", "panela-food-burger.jpg"),
    ("Construtora Coruja", "construtora-coruja.jpg"),
    ("Genuino Construtora", "genuino-construtora.jpg"),
    ("Construtora Panassolo", "construtora-panassolo.jpg"),
    ("Sardi Galaschi Incorporadora", "sardi-galaschi.jpg"),
    ("Select Construtora e Incorporadora", "select-construtora.jpg"),
    ("Contemporânea Construtora", "contemporanea-construtora.jpg"),
    ("LS Administradora Predial", "ls-administradora.jpg"),
    ("Constru Matta", "constru-matta.jpg"),
]

MEMBER_AGENCIES = [
    ("RE/MAX Rede Prime Litoral", "remax-rede-prime-litoral.jpg"),
    ("MW Imobiliária e Construtora", "mw-imobiliaria.png"),
    ("Cia da Praia Imobiliária", "cia-da-praia.png"),
    ("BeachHouse Imobiliária", "beachhouse.png"),
    ("Inova Serviços Imobiliários", "inova.png"),
    ("DTX Imóveis", "dtx-imoveis.png"),
]


class Command(BaseCommand):
    help = (
        "Semeia os parceiros comerciais e as imobiliárias associadas "
        "conhecidas (conteúdo de referência do PRD), com logos."
    )

    def handle(self, *args, **options):
        created = 0
        for order, (name, logo) in enumerate(PARTNERS, start=1):
            partner, was_created = Partner.objects.update_or_create(
                name=name,
                defaults={"kind": Partner.Kind.PARTNER, "order": order},
            )
            attach_image(partner, "logo", "partners", logo)
            created += was_created

        for order, (name, logo) in enumerate(MEMBER_AGENCIES, start=1):
            partner, was_created = Partner.objects.update_or_create(
                name=name,
                defaults={"kind": Partner.Kind.MEMBER_AGENCY, "order": order},
            )
            attach_image(partner, "logo", "agencies", logo)
            created += was_created

        self.stdout.write(self.style.SUCCESS(f"Parceiros semeados ({created} novos registros)."))
