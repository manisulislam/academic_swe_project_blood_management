from django import forms
from core.models import ContactMessage
from .models import BloodStock
class StockForm(forms.Form):
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    blood_group = forms.ChoiceField(
        choices=BLOOD_GROUP_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    units = forms.IntegerField(
        min_value=0,  # allow 0 units
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter number of units'})
    )

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5}),
        }