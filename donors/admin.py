from django.contrib import admin
from .models import DonorProfile

@admin.register(DonorProfile)
class DonorProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'blood_group', 'city', 'eligible_for_donation', 'last_donation_date')
    list_filter = ('blood_group', 'city', 'eligible_for_donation')
    search_fields = ('user__username', 'user__email', 'city')
    ordering = ('user__username',)
    
    # Show diseases and allergies in form
    fieldsets = (
        ('Personal Info', {
            'fields': ('user', 'city', 'contact_number')
        }),
        ('Medical Info', {
            'fields': ('blood_group', 'diseases', 'allergies')
        }),
        ('Donation Info', {
            'fields': ('last_donation_date', 'eligible_for_donation')
        }),
    )

    filter_horizontal = ()  # Not needed for MultiSelectField, only for ManyToManyField
