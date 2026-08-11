from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from .models import Post


def post_list(request):
    posts = Post.objects.filter(status=Post.Status.PUBLISHED)
    paginator = Paginator(posts, 6)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)

    context = {"page_obj": page_obj}
    template = "blog/partials/_post_list.html" if request.htmx else "blog/list.html"
    return render(request, template, context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status=Post.Status.PUBLISHED)
    return render(request, "blog/detail.html", {"post": post})
