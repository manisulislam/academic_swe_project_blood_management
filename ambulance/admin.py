from django.contrib import admin
from .models import Ambulance, AmbulanceRequest

@admin.register(Ambulance)
class AmbulanceAdmin(admin.ModelAdmin):
    list_display = ("number_plate", "driver_name", "phone", "available", "location")
    list_filter = ("available",)
    search_fields = ("number_plate", "driver_name", "phone")
    ordering = ("number_plate",)

    fieldsets = (
        ("Ambulance Information", {
            "fields": ("number_plate", "driver_name", "phone", "available", "location")
        }),
    )


@admin.register(AmbulanceRequest)
class AmbulanceRequestAdmin(admin.ModelAdmin):
    list_display = ("user", "ambulance", "pickup_location", "destination", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("user__username", "ambulance__number_plate", "pickup_location", "destination")
    date_hierarchy = "created_at"
    ordering = ("-created_at",)

    readonly_fields = ("created_at",)
    fieldsets = (
        ("Request Information", {
            "fields": ("user", "ambulance", "pickup_location", "destination", "emergency_type", "status", "created_at")
        }),
    )
