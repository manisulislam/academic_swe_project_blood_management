from django.contrib import admin
from .models import BloodStock

@admin.register(BloodStock)
class BloodStockAdmin(admin.ModelAdmin):
    list_display = ['blood_group', 'units']
    search_fields = ['blood_group']
