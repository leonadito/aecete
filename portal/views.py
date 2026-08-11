from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import PortalAuthenticationForm, PriceTableForm
from .models import PriceTable


def is_builder(user):
    return user.is_authenticated and hasattr(user, "builder") and user.builder.is_active


def is_broker(user):
    return user.is_authenticated and (
        user.is_staff or user.groups.filter(name="Corretores").exists()
    )


class BuilderLoginView(auth_views.LoginView):
    template_name = "portal/builder_login.html"
    authentication_form = PortalAuthenticationForm

    def form_valid(self, form):
        if not is_builder(form.get_user()):
            form.add_error(None, "Este acesso é exclusivo para construtoras.")
            return self.form_invalid(form)
        return super().form_valid(form)

    def get_success_url(self):
        return str(reverse_lazy("portal:builder_dashboard"))


class BrokerLoginView(auth_views.LoginView):
    template_name = "portal/broker_login.html"
    authentication_form = PortalAuthenticationForm

    def form_valid(self, form):
        if not is_broker(form.get_user()):
            form.add_error(None, "Este acesso é exclusivo para corretores e imobiliárias associadas.")
            return self.form_invalid(form)
        return super().form_valid(form)

    def get_success_url(self):
        return str(reverse_lazy("portal:broker_price_table_list"))


class BuilderRequiredMixin(UserPassesTestMixin):
    login_url = reverse_lazy("portal:builder_login")

    def test_func(self):
        return is_builder(self.request.user)


class BrokerRequiredMixin(UserPassesTestMixin):
    login_url = reverse_lazy("portal:broker_login")

    def test_func(self):
        return is_broker(self.request.user)


class BuilderDashboardView(BuilderRequiredMixin, ListView):
    model = PriceTable
    template_name = "portal/builder_dashboard.html"
    context_object_name = "price_tables"

    def get_queryset(self):
        return PriceTable.objects.filter(builder=self.request.user.builder)


class PriceTableCreateView(BuilderRequiredMixin, CreateView):
    model = PriceTable
    form_class = PriceTableForm
    template_name = "portal/price_table_form.html"
    success_url = reverse_lazy("portal:builder_dashboard")

    def form_valid(self, form):
        form.instance.builder = self.request.user.builder
        return super().form_valid(form)


class PriceTableUpdateView(BuilderRequiredMixin, UpdateView):
    model = PriceTable
    form_class = PriceTableForm
    template_name = "portal/price_table_form.html"
    success_url = reverse_lazy("portal:builder_dashboard")

    def get_queryset(self):
        return PriceTable.objects.filter(builder=self.request.user.builder)


class PriceTableDeleteView(BuilderRequiredMixin, DeleteView):
    model = PriceTable
    template_name = "portal/price_table_confirm_delete.html"
    success_url = reverse_lazy("portal:builder_dashboard")

    def get_queryset(self):
        return PriceTable.objects.filter(builder=self.request.user.builder)


class BrokerPriceTableListView(BrokerRequiredMixin, ListView):
    model = PriceTable
    template_name = "portal/broker_price_table_list.html"
    context_object_name = "price_tables"
    paginate_by = 9

    def get_queryset(self):
        return (
            PriceTable.objects.filter(is_active=True, builder__is_active=True)
            .select_related("builder")
        )

    def get_template_names(self):
        if self.request.htmx:
            return ["portal/partials/_price_table_list.html"]
        return [self.template_name]
