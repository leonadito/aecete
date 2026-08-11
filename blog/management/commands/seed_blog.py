from django.core.management.base import BaseCommand
from django.utils import timezone

from blog.models import Post
from pages.seed_utils import attach_image


class Command(BaseCommand):
    help = "Semeia o post 'Nova Diretoria da AICITI', migrado do blog do site atual."

    def handle(self, *args, **options):
        post, created = Post.objects.update_or_create(
            slug="nova-diretoria-da-aiciti",
            defaults={
                "title": "Nova Diretoria da AICITI",
                "content": "Conheça a nova diretoria da AICITI.",
                "status": Post.Status.PUBLISHED,
                "is_featured": True,
                "published_at": post_published_at(),
            },
        )
        attach_image(post, "cover_image", "blog", "nova-diretoria.jpg")

        if created:
            self.stdout.write(self.style.SUCCESS(f"Post criado: {post.title}"))
        else:
            self.stdout.write("Post já existia — atualizado.")


def post_published_at():
    return timezone.make_aware(timezone.datetime(2023, 5, 6, 12, 0))
