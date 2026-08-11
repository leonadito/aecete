from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Builder, PriceTable


class PriceTableInline(admin.TabularInline):
    model = PriceTable
    extra = 0
    template = "portal/edit_inline/pricetable_tabular.html"
    fields = (
        ("title", "description", "image", "drive_link"),
        ("is_active", "created_at"),
    )
    readonly_fields = ("created_at",)

    class Media:
        css = {"all": ("portal/admin_inline.css",)}


@admin.register(Builder)
class BuilderAdmin(admin.ModelAdmin):
    # Provisionamento manual: crie o User (com login/senha) no admin de
    # usuários primeiro, depois crie o Builder aqui selecionando esse User.
    list_display = ("name", "user", "is_active", "created_at")
    list_filter = ("is_active",)
    search_fields = ("name", "user__username")
    autocomplete_fields = ("user",)
    inlines = [PriceTableInline]


@admin.register(PriceTable)
class PriceTableAdmin(admin.ModelAdmin):
    list_display = ("title", "builder", "is_active", "created_at")
    list_filter = ("is_active", "builder")
    search_fields = ("title", "builder__name")


class UserAdmin(BaseUserAdmin):
    # Portal access is granted two different ways (see CLAUDE.md): a Builder
    # record pointing at the user, or membership in the Corretores group.
    # Neither is obvious from the stock user list, so surface it here.
    list_display = BaseUserAdmin.list_display + ("portal_access",)

    @admin.display(description="Acesso no portal")
    def portal_access(self, obj):
        if hasattr(obj, "builder"):
            return "Construtora"
        if obj.groups.filter(name="Corretores").exists():
            return "Corretor/imobiliária"
        return "—"


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
