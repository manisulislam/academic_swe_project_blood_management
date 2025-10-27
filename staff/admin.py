from django.contrib import admin
from .models import Staff

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ("user", "department", "phone", "shift")
    list_filter = ("department", "shift")
    search_fields = ("user__username", "user__first_name", "user__last_name", "phone")
    ordering = ("department", "user__username")

    fieldsets = (
        ("Staff Information", {
            "fields": ("user", "department", "phone", "shift")
        }),
    )

    def get_queryset(self, request):
        """Optional: Show only staff users."""
        qs = super().get_queryset(request)
        return qs.filter(user__role="staff")
