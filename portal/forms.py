from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import PriceTable

_INPUT_CLASS = (
    "block w-full rounded-lg border border-slate-300 pl-10 pr-3 py-2 "
    "focus:border-brand focus:ring-brand sm:text-sm"
)


class PortalAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label="Usuário",
        widget=forms.TextInput(attrs={"class": _INPUT_CLASS, "autofocus": True}),
    )
    password = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(attrs={"class": _INPUT_CLASS}),
    )


class PriceTableForm(forms.ModelForm):
    class Meta:
        model = PriceTable
        fields = ["title", "description", "image", "drive_link"]
        widgets = {
            "title": forms.TextInput(
                attrs={"placeholder": "Nome da tabela", "class": _INPUT_CLASS}
            ),
            "description": forms.Textarea(
                attrs={"placeholder": "Descrição", "rows": 4, "class": _INPUT_CLASS}
            ),
            "drive_link": forms.URLInput(
                attrs={"placeholder": "Link do drive", "class": _INPUT_CLASS}
            ),
        }
