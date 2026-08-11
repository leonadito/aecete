from django.shortcuts import render

from .models import Partner


def partner_list(request):
    context = {
        "partners": Partner.objects.filter(kind=Partner.Kind.PARTNER, is_active=True),
    }
    return render(request, "partners/list.html", context)
