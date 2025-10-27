from django.db import models
from django.conf import settings

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    stock = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    expiry_date = models.DateField()
    reorder_level = models.IntegerField(default=10)

    def __str__(self):
        return self.name


class MedicineOrder(models.Model):
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'role': 'patient'})
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=20, default="Pending")  # Pending, Delivered
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.username} - {self.medicine.name}"
