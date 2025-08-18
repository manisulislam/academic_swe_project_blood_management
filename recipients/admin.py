from django.contrib import admin
from .models import BloodRequest

@admin.register(BloodRequest)
class BloodRequestAdmin(admin.ModelAdmin):
    list_display = ['user', 'blood_group', 'units', 'status', 'requested_on']
    list_filter = ['status', 'blood_group']
    search_fields = ['user__username', 'blood_group']
