from django.db import models
from django.conf import settings

class DonorProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=5)
    last_donation_date = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} – {self.blood_group}"
