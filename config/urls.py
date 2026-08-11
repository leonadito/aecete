from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from django.views.generic import TemplateView

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

# Served unconditionally (not just in DEBUG): this low-traffic site has no
# separate nginx/CDN in front of it, so gunicorn serving /media/ directly is
# the simplest correct option, same reasoning as using WhiteNoise for /static/.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
