from django.contrib import admin
from .models import Test, LabReport

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "description_short")
    search_fields = ("name",)
    list_filter = ("price",)
    ordering = ("name",)

    def description_short(self, obj):
        """Show first 50 chars of description."""
        return (obj.description[:50] + "...") if len(obj.description) > 50 else obj.description
    description_short.short_description = "Description"


@admin.register(LabReport)
class LabReportAdmin(admin.ModelAdmin):
    list_display = ("test", "patient", "uploaded_at", "file_link")
    search_fields = ("test__name", "patient__username")
    list_filter = ("uploaded_at", "test")
    date_hierarchy = "uploaded_at"
    ordering = ("-uploaded_at",)

    fieldsets = (
        ("Report Details", {
            "fields": ("test", "patient", "file", "uploaded_at")
        }),
    )

    readonly_fields = ("uploaded_at", "file_link")

    def file_link(self, obj):
        """Show a clickable link to the uploaded file in admin."""
        if obj.file:
            return f"<a href='{obj.file.url}' target='_blank'>View Report</a>"
        return "No File"
    file_link.allow_tags = True
    file_link.short_description = "Report File"
