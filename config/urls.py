from django.conf import settings
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from django.views.generic import TemplateView
from django.views.static import serve as serve_static

from pages.sitemaps import BlogPostSitemap, StaticViewSitemap

sitemaps = {
    "static": StaticViewSitemap,
    "blog": BlogPostSitemap,
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("pages.urls")),
    path("parceiros/", include("partners.urls")),
    path("blog/", include("blog.urls")),
    path("contato/", include("contact.urls")),
    path("acessos/", include("portal.urls")),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
        name="robots_txt",
    ),
]

# django.conf.urls.static.static() silently returns [] whenever DEBUG is
# False (a check baked into the helper itself, not just typical call-site
# usage) so it can't serve /media/ in production. This site has no separate
# nginx/CDN in front of it, so wire django.views.static.serve directly
# instead — same trade-off already made for /static/ via WhiteNoise.
urlpatterns += [
    path(
        f"{settings.MEDIA_URL.lstrip('/')}<path:path>",
        serve_static,
        {"document_root": settings.MEDIA_ROOT},
    ),
]
