from django.db import models
from django.conf import settings

class Appointment(models.Model):
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="doctor_appointments", limit_choices_to={'role': 'doctor'})
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="patient_appointments", limit_choices_to={'role': 'patient'})
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=20, default="Scheduled")  # Scheduled, Completed, Cancelled
    reason = models.TextField(blank=True)

    def __str__(self):
        return f"{self.patient.username} with {self.doctor.username} on {self.date}"
