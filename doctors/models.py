from django.db import models
from django.conf import settings  # for AUTH_USER_MODEL

class Doctor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'role': 'doctor'})
    specialization = models.CharField(max_length=150)
    qualification = models.CharField(max_length=200)
    chamber_time = models.CharField(max_length=100)

    def __str__(self):
        return f"Dr. {self.user.get_full_name() or self.user.username}"
