from django.core.management.base import BaseCommand

from pages.models import FAQItem

FAQ_ITEMS = [
    (
        "O que é a AICITI?",
        "Associação das Imobiliárias e Corretores de Imóveis de Tramandaí e Imbé, que "
        "representa e fortalece a classe imobiliária regional, promovendo ética "
        "profissional e desenvolvimento de mercado.",
    ),
    (
        "Quem pode se associar à AICITI?",
        "Imobiliárias constituídas legalmente e corretores registrados no CRECI que "
        "atuem em Tramandaí e Imbé, incluindo profissionais autônomos.",
    ),
    (
        "Quais são as vantagens de ser associado?",
        "Acesso a convênios exclusivos, capacitação profissional, eventos de "
        "networking, representação institucional e benefícios comerciais.",
    ),
    (
        "A AICITI oferece capacitação?",
        "Sim, promove palestras, workshops e cursos sobre práticas de mercado, "
        "inovação, vendas, legislação e tecnologias imobiliárias.",
    ),
    (
        "A associação defende interesses da categoria?",
        "A AICITI é representante oficial, atuando junto a entidades públicas e "
        "privadas para garantir direitos e promover um mercado justo.",
    ),
    (
        "Que tipos de convênios oferece?",
        "Assessoria jurídica, cursos com desconto, comunicação/marketing, soluções "
        "tecnológicas (CRM) e materiais de divulgação.",
    ),
    (
        "Como se associar?",
        "Contatar a diretoria, preencher ficha de cadastro, apresentar documentação "
        "e aguardar aprovação.",
    ),
    (
        "Quais as responsabilidades do associado?",
        "Seguir código de ética, atuar com transparência, participar de reuniões e "
        "manter contribuições em dia.",
    ),
    (
        "A AICITI organiza eventos?",
        "Sim, promove encontros periódicos, seminários e feiras que geram "
        "networking e compartilham tendências do mercado.",
    ),
]


class Command(BaseCommand):
    help = "Semeia as 9 perguntas frequentes (conteúdo completo do PRD)."

    def handle(self, *args, **options):
        created = 0
        for order, (question, answer) in enumerate(FAQ_ITEMS, start=1):
            _, was_created = FAQItem.objects.update_or_create(
                question=question,
                defaults={"answer": answer, "order": order},
            )
            created += was_created

        self.stdout.write(self.style.SUCCESS(f"FAQ semeado ({created} novos registros)."))
