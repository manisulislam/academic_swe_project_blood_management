from django.db import models
from django.conf import settings

class Staff(models.Model):
    DEPARTMENT_CHOICES = (
        ('reception', 'Reception'),
        ('billing', 'Billing'),
        ('lab', 'Laboratory'),
        ('pharmacy', 'Pharmacy'),
        ('ambulance', 'Ambulance'),
        ('other', 'Other'),
    )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'staff'}
    )
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES, default='other')
    phone = models.CharField(max_length=15, blank=True, null=True)
    shift = models.CharField(max_length=50, blank=True, null=True)  # e.g., Morning, Evening, Night

    def __str__(self):
        return f"{self.user.get_full_name() or self.user.username} ({self.department})"
