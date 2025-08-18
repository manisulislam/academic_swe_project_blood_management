from django.db import models

class BloodStock(models.Model):
    blood_group = models.CharField(max_length=5, unique=True)
    units = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.blood_group} — {self.units} units"
