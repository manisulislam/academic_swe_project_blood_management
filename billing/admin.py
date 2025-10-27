from django.contrib import admin
from .models import Invoice

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ("id", "patient", "amount", "status", "created_at", "description_short")
    list_filter = ("status", "created_at")
    search_fields = ("patient__username", "description")
    date_hierarchy = "created_at"
    ordering = ("-created_at",)

    readonly_fields = ("created_at",)
    fieldsets = (
        ("Invoice Information", {
            "fields": ("patient", "amount", "description", "status", "created_at")
        }),
    )

    def description_short(self, obj):
        """Display first 50 characters of description for admin list."""
        return (obj.description[:50] + "...") if len(obj.description) > 50 else obj.description
    description_short.short_description = "Description"
