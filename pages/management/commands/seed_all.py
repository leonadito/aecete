from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Roda todos os seeds de conteúdo institucional (diretoria, benefícios, FAQ, parceiros, blog)."

    def handle(self, *args, **options):
        call_command("seed_board")
        call_command("seed_benefits")
        call_command("seed_faq")
        call_command("seed_partners")
        call_command("seed_blog")
        self.stdout.write(self.style.SUCCESS("Seed completo."))
