from django.conf import settings
from django.urls import reverse


def site_info(request):
    """Shared header/footer/contact data, available in every template."""
    user = request.user
    is_builder = user.is_authenticated and hasattr(user, "builder") and user.builder.is_active
    is_broker = user.is_authenticated and (
        user.is_staff or user.groups.filter(name="Corretores").exists()
    )

    if is_builder:
        access_children = [
            {"label": "Minha área", "url": reverse("portal:builder_dashboard")},
            {"label": "Sair", "url": reverse("portal:logout"), "method": "post"},
        ]
    elif is_broker:
        access_children = [
            {"label": "Minha área", "url": reverse("portal:broker_price_table_list")},
            {"label": "Sair", "url": reverse("portal:logout"), "method": "post"},
        ]
    else:
        access_children = [
            {"label": "Área das construtoras", "url": reverse("portal:builder_login")},
            {"label": "Área dos corretores", "url": reverse("portal:broker_login")},
        ]
    access_children.append(
        {
            "label": "Acesso ao Roll",
            "url": "https://tramandai.aiciti.com.br/login?logout",
            "external": True,
        }
    )

    nav_items = [
        {"label": "Página inicial", "url": reverse("pages:home")},
        {"label": "Sobre", "url": reverse("pages:about")},
        {"label": "Benefícios", "url": reverse("pages:benefits")},
        {"label": "Parceiros", "url": reverse("partners:list")},
        {"label": "Dúvidas", "url": reverse("pages:faq")},
        {"label": "Blog", "url": reverse("blog:post_list")},
        {"label": "Contato", "url": reverse("contact:page")},
        {"label": "Acessos", "children": access_children},
    ]
    return {
        "nav_items": nav_items,
        "site_name": settings.SITE_NAME,
        "site_phone_display": settings.SITE_PHONE_DISPLAY,
        "site_phone_whatsapp": settings.SITE_PHONE_WHATSAPP,
        "site_address": settings.SITE_ADDRESS,
        "site_facebook_url": settings.SITE_FACEBOOK_URL,
        "site_instagram_url": settings.SITE_INSTAGRAM_URL,
    }
