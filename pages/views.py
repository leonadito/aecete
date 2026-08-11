from blog.models import Post
from partners.models import Partner
from django.shortcuts import render

from .models import Benefit, BoardMember, FAQItem


def home(request):
    featured_posts = list(Post.objects.filter(status=Post.Status.PUBLISHED, is_featured=True)[:3])
    if len(featured_posts) < 3:
        extra_ids = [p.id for p in featured_posts]
        extra = Post.objects.filter(status=Post.Status.PUBLISHED).exclude(
            id__in=extra_ids
        )[: 3 - len(featured_posts)]
        featured_posts += list(extra)

    context = {
        "benefits": Benefit.objects.all(),
        "board_members": BoardMember.objects.filter(group=BoardMember.Group.DIRETORIA),
        "member_agencies": Partner.objects.filter(
            kind=Partner.Kind.MEMBER_AGENCY, is_active=True
        ),
        "posts": featured_posts,
    }
    return render(request, "pages/home.html", context)


def about(request):
    context = {
        "diretoria": BoardMember.objects.filter(group=BoardMember.Group.DIRETORIA),
        "titulares": BoardMember.objects.filter(group=BoardMember.Group.TITULAR),
        "suplentes": BoardMember.objects.filter(group=BoardMember.Group.SUPLENTE),
    }
    return render(request, "pages/about.html", context)


def benefits(request):
    context = {"benefits": Benefit.objects.all()}
    return render(request, "pages/benefits.html", context)


def faq(request):
    context = {"faq_items": FAQItem.objects.all()}
    return render(request, "pages/faq.html", context)
