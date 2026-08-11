from django.contrib import admin

from .models import Partner


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ("name", "kind", "is_active", "order")
    list_filter = ("kind", "is_active")
    list_editable = ("order", "is_active")
    search_fields = ("name",)
