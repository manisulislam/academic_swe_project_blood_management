from django.db import models
from django.conf import settings

class Test(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class LabReport(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'role': 'patient'})
    file = models.FileField(upload_to="lab_reports/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.test.name} - {self.patient.username}"
