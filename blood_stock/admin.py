from django.contrib import admin
from .models import BloodStock

@admin.register(BloodStock)
class BloodStockAdmin(admin.ModelAdmin):
    list_display = ('blood_group', 'units')       # Table view in admin
    list_editable = ('units',)                    # Units can be updated directly in list view
    ordering = ('blood_group',)                   # Order by blood group
    search_fields = ('blood_group',)             # Search by blood group
