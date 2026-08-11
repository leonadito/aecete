from django.core.management.base import BaseCommand

from pages.models import BoardMember
from pages.seed_utils import attach_image

DIRETORIA = [
    ("Thiago Kury", "Presidente", "thiago-kury.jpg"),
    ("Marlon Alves", "Vice-Presidente", "marlon-alves.jpg"),
    ("Patricia Beck", "1ª Secretária", "patricia-beck.jpg"),
    ("Jonas Rosa", "2º Secretário", "jonas-rosa.jpg"),
    ("Cicero Severo", "1º Tesoureiro", "cicero-severo.jpg"),
    ("Mana Brochier", "2ª Tesoureira", "mana-brochier.jpg"),
]

TITULARES = [
    ("Alfeu Barros", "alfeu-barros.jpg"),
    ("Carlos Henrique", "carlos-henrique.jpg"),
    ("Alessandra Wagner", "alessandra-wagner.jpg"),
    ("Danubia Firme", "danubia-firme.jpg"),
    ("Eduardo Wypyszinski", "eduardo-wypyszinski.jpg"),
    ("Indiana Barbosa", "indiana-barbosa.jpg"),
]

SUPLENTES = [
    ("Rafael Britto", "rafael-britto.jpg"),
    ("Tiago Schmals", "tiago-schmals.jpg"),
    ("Natascha Motta", "natascha-motta.jpg"),
]


class Command(BaseCommand):
    help = "Semeia a diretoria da AICITI (conteúdo de referência do PRD), com fotos."

    def handle(self, *args, **options):
        created = 0
        for order, (name, role, photo) in enumerate(DIRETORIA, start=1):
            member, was_created = BoardMember.objects.update_or_create(
                name=name,
                defaults={
                    "role": role,
                    "group": BoardMember.Group.DIRETORIA,
                    "order": order,
                },
            )
            attach_image(member, "photo", "board", photo)
            created += was_created

        for order, (name, photo) in enumerate(TITULARES, start=1):
            member, was_created = BoardMember.objects.update_or_create(
                name=name,
                defaults={"role": "", "group": BoardMember.Group.TITULAR, "order": order},
            )
            attach_image(member, "photo", "board", photo)
            created += was_created

        for order, (name, photo) in enumerate(SUPLENTES, start=1):
            member, was_created = BoardMember.objects.update_or_create(
                name=name,
                defaults={"role": "", "group": BoardMember.Group.SUPLENTE, "order": order},
            )
            attach_image(member, "photo", "board", photo)
            created += was_created

        self.stdout.write(self.style.SUCCESS(f"Diretoria semeada ({created} novos registros)."))
