from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("doctor", "patient", "date", "time", "status", "reason_short")
    list_filter = ("status", "date", "doctor")
    search_fields = ("doctor__username", "patient__username", "reason")
    date_hierarchy = "date"
    ordering = ("-date", "time")

    readonly_fields = ()

    fieldsets = (
        ("Appointment Information", {
            "fields": ("doctor", "patient", "date", "time", "status", "reason")
        }),
    )

    def reason_short(self, obj):
        """Show first 50 chars of reason."""
        return (obj.reason[:50] + "...") if len(obj.reason) > 50 else obj.reason
    reason_short.short_description = "Reason"
