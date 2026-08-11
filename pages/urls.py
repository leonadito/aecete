from django.urls import path

from . import views

app_name = "pages"

urlpatterns = [
    path("", views.home, name="home"),
    path("sobre/", views.about, name="about"),
    path("beneficios/", views.benefits, name="benefits"),
    path("duvidas/", views.faq, name="faq"),
]
