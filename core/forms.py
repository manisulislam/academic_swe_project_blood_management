from django import forms
from .models import Announcement , ContactMessage
class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'content', 'is_urgent', 'expiry_date', 'attachment']
        widgets = {
            'expiry_date': forms.DateInput(attrs={'type': 'date'}),
            'content': forms.Textarea(attrs={'rows': 5}),
        }


