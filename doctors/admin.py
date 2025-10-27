from django.contrib import admin
from .models import Doctor

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("user", "specialization", "qualification", "chamber_time")
    list_filter = ("specialization",)
    search_fields = ("user__username", "user__first_name", "user__last_name", "specialization", "qualification")
    ordering = ("user__username",)

    fieldsets = (
        ("Doctor Information", {
            "fields": ("user", "specialization", "qualification", "chamber_time")
        }),
    )

    def get_queryset(self, request):
        """Show only users with role=doctor."""
        qs = super().get_queryset(request)
        return qs.filter(user__role="doctor")
