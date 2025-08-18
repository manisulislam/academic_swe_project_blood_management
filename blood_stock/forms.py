from django import forms
from core.models import ContactMessage
class StockForm(forms.Form):
    blood_group = forms.CharField(max_length=5)
    units = forms.IntegerField(min_value=1)

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5}),
        }