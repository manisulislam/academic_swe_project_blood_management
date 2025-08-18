from django.db import models
from django.conf import settings
from multiselectfield import MultiSelectField

class DonorProfile(models.Model):
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

    DISEASE_CHOICES = [
        ('diabetes', 'Diabetes'),
        ('hypertension', 'Hypertension'),
        ('asthma', 'Asthma'),
        ('thyroid', 'Thyroid'),
        ('heart_disease', 'Heart Disease'),
        ('none', 'None'),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES)
    last_donation_date = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=100)

    # Use MultiSelectField to allow multiple diseases
    diseases = MultiSelectField(choices=DISEASE_CHOICES, max_length=200, blank=True)
    allergies = models.TextField(null=True, blank=True, help_text="Any known allergies")
    contact_number = models.CharField(max_length=15, null=True, blank=True)
    eligible_for_donation = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} – {self.blood_group}"
