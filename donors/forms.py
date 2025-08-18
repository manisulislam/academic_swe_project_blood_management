from django import forms
from .models import DonorProfile

class DonorProfileForm(forms.ModelForm):
    class Meta:
        model = DonorProfile
        fields = ['blood_group', 'last_donation_date', 'city']
        widgets = {
            'last_donation_date': forms.DateInput(attrs={'type': 'date'}),
        }
