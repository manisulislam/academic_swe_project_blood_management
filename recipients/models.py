from django.db import models
from django.conf import settings

class BloodRequest(models.Model):
    BLOOD_STATUS = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )
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

    URGENCY_CHOICES = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES)
    units = models.PositiveIntegerField()
    hospital = models.CharField(max_length=150, null=True, blank=True)   # new field
    urgency = models.CharField(max_length=10, choices=URGENCY_CHOICES, default='medium')
    request_date = models.DateField(auto_now_add=False, null=True, blank=True)
    request_time = models.TimeField(auto_now_add=False, null=True, blank=True)
    reason = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=BLOOD_STATUS, default='pending')
    requested_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} – {self.blood_group} ({self.units} units)"
