from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from blog.models import Post


class StaticViewSitemap(Sitemap):
    priority = 0.6
    changefreq = "monthly"

    def items(self):
        return [
            "pages:home",
            "pages:about",
            "pages:benefits",
            "pages:faq",
            "partners:list",
            "blog:post_list",
            "contact:page",
        ]

    def location(self, item):
        return reverse(item)


class BlogPostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Post.objects.filter(status=Post.Status.PUBLISHED)

    def lastmod(self, obj):
        return obj.updated_at
