from django.contrib import admin
from .models import DonorProfile

@admin.register(DonorProfile)
class DonorProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'blood_group', 'city', 'last_donation_date']
    search_fields = ['user__username', 'blood_group', 'city']
