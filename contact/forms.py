from django import forms

from .models import ContactMessage


_INPUT_CLASS = (
    "block w-full rounded-lg border border-slate-300 pl-10 pr-3 py-2 "
    "focus:border-brand focus:ring-brand sm:text-sm"
)


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "phone", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Seu nome", "class": _INPUT_CLASS}),
            "email": forms.EmailInput(attrs={"placeholder": "Seu e-mail", "class": _INPUT_CLASS}),
            "phone": forms.TextInput(
                attrs={"placeholder": "Seu telefone (opcional)", "class": _INPUT_CLASS}
            ),
            "message": forms.Textarea(
                attrs={"placeholder": "Sua mensagem", "rows": 5, "class": _INPUT_CLASS}
            ),
        }

    def clean_message(self):
        message = self.cleaned_data["message"].strip()
        if len(message) < 10:
            raise forms.ValidationError("Conte um pouco mais na sua mensagem.")
        return message
