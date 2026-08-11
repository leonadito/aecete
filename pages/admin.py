from django.contrib import admin

from .models import Benefit, BoardMember, FAQItem


@admin.register(BoardMember)
class BoardMemberAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "group", "order")
    list_filter = ("group",)
    list_editable = ("order",)
    search_fields = ("name", "role")


@admin.register(Benefit)
class BenefitAdmin(admin.ModelAdmin):
    list_display = ("title", "icon", "order")
    list_editable = ("order",)
    search_fields = ("title",)


@admin.register(FAQItem)
class FAQItemAdmin(admin.ModelAdmin):
    list_display = ("question", "order")
    list_editable = ("order",)
    search_fields = ("question", "answer")
