from django.db import models
from django.conf import settings

class BloodRequest(models.Model):
    BLOOD_STATUS = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=5)
    units = models.PositiveIntegerField()
    status = models.CharField(max_length=10, choices=BLOOD_STATUS, default='pending')
    requested_on = models.DateTimeField(auto_now_add=True)
