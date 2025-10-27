from django.db import models
from django.conf import settings

class Ambulance(models.Model):
    number_plate = models.CharField(max_length=20, unique=True)
    driver_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    available = models.BooleanField(default=True)
    location = models.CharField(max_length=255, blank=True, null=True)  # optional GPS field

    def __str__(self):
        return f"Ambulance {self.number_plate} - {'Available' if self.available else 'Busy'}"


class AmbulanceRequest(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ambulance = models.ForeignKey(Ambulance, on_delete=models.SET_NULL, null=True, blank=True)
    pickup_location = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    emergency_type = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=20, default="Pending")  # Pending, Accepted, Completed
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Request by {self.user.username} ({self.status})"
