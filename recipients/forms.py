from django import forms
from .models import BloodRequest

class BloodRequestForm(forms.ModelForm):
    request_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        required=True
    )
    request_time = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        required=True
    )

    class Meta:
        model = BloodRequest
        fields = [
            'blood_group', 'units', 'hospital', 'urgency', 'reason',
            'request_date', 'request_time'
        ]
        widgets = {
            'blood_group': forms.Select(attrs={'class': 'form-control'}),
            'units': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'hospital': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hospital name or location'}),
            'urgency': forms.Select(attrs={'class': 'form-control'}),
            'reason': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Reason for request'}),
        }
