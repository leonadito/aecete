from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = "portal"

urlpatterns = [
    path("construtoras/login/", views.BuilderLoginView.as_view(), name="builder_login"),
    path("construtoras/", views.BuilderDashboardView.as_view(), name="builder_dashboard"),
    path(
        "construtoras/tabelas/nova/",
        views.PriceTableCreateView.as_view(),
        name="price_table_create",
    ),
    path(
        "construtoras/tabelas/<int:pk>/editar/",
        views.PriceTableUpdateView.as_view(),
        name="price_table_update",
    ),
    path(
        "construtoras/tabelas/<int:pk>/excluir/",
        views.PriceTableDeleteView.as_view(),
        name="price_table_delete",
    ),
    path("corretores/login/", views.BrokerLoginView.as_view(), name="broker_login"),
    path(
        "corretores/",
        views.BrokerPriceTableListView.as_view(),
        name="broker_price_table_list",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(next_page="pages:home"),
        name="logout",
    ),
]
