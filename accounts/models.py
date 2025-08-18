from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('donor', 'Donor'),
        ('recipient', 'Recipient'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='recipient')

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
