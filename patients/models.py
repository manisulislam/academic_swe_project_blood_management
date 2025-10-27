from django.db import models
from django.conf import settings

class Patient(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'role': 'patient'})
    blood_group = models.CharField(max_length=5, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
