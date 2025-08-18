from django import forms
from .models import DonorProfile

class DonorProfileForm(forms.ModelForm):
    last_donation_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        required=False
    )
    
    city = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your city'})
    )
    
    blood_group = forms.ChoiceField(
        choices=DonorProfile.BLOOD_GROUP_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    diseases = forms.MultipleChoiceField(
        choices=DonorProfile.DISEASE_CHOICES,  # Show predefined options
        widget=forms.CheckboxSelectMultiple(),
        required=False
    )
    
    allergies = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Any known allergies'}),
        required=False
    )
    
    contact_number = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+8801XXXXXXXXX'}),
        required=False
    )
    
    eligible_for_donation = forms.BooleanField(
        required=False,
        initial=True,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

    class Meta:
        model = DonorProfile
        fields = [
            'blood_group', 'last_donation_date', 'city', 
            'diseases', 'allergies', 'contact_number', 'eligible_for_donation'
        ]
