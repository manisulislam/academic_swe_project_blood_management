from django.contrib import admin
from .models import Medicine, MedicineOrder

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ("name", "stock", "price", "expiry_date", "reorder_level", "needs_reorder")
    search_fields = ("name",)
    list_filter = ("expiry_date",)
    ordering = ("name",)

    def needs_reorder(self, obj):
        """Show if the medicine stock is below reorder level."""
        return obj.stock <= obj.reorder_level
    needs_reorder.boolean = True
    needs_reorder.short_description = "Needs Reorder"


@admin.register(MedicineOrder)
class MedicineOrderAdmin(admin.ModelAdmin):
    list_display = ("patient", "medicine", "quantity", "status", "created_at")
    search_fields = ("patient__username", "medicine__name")
    list_filter = ("status", "created_at")
    date_hierarchy = "created_at"
    ordering = ("-created_at",)

    readonly_fields = ("created_at",)
    fieldsets = (
        ("Order Information", {
            "fields": ("patient", "medicine", "quantity", "status", "created_at")
        }),
    )
