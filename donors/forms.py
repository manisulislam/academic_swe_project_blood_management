from django import forms
from datetime import date, timedelta
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
        choices=DonorProfile.DISEASE_CHOICES,
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

    # ✅ Validation: Enforce 3 months wait
    def clean(self):
        cleaned_data = super().clean()
        last_donation_date = cleaned_data.get("last_donation_date")
        eligible = cleaned_data.get("eligible_for_donation")

        if last_donation_date:
            min_next_donation = last_donation_date + timedelta(days=90)
            if date.today() < min_next_donation:
                raise forms.ValidationError(
                    f"You can donate again only after {min_next_donation.strftime('%d %B %Y')}."
                )

        # If not eligible, make sure checkbox is False
        if last_donation_date and date.today() < (last_donation_date + timedelta(days=90)):
            cleaned_data["eligible_for_donation"] = False

        return cleaned_data
