from django.shortcuts import render, redirect
from .models import Appointment
from django.contrib.auth.decorators import login_required

@login_required
def create_appointment(request):
    if request.method == "POST":
        doctor_id = request.POST.get("doctor")
        date = request.POST.get("date")
        time = request.POST.get("time")
        Appointment.objects.create(
            doctor_id=doctor_id,
            patient=request.user,
            date=date,
            time=time
        )
        return redirect("appointment_list")
    return render(request, "appointments/create.html")

@login_required
def appointment_list(request):
    if request.user.role == "doctor":
        appointments = Appointment.objects.filter(doctor=request.user)
    else:
        appointments = Appointment.objects.filter(patient=request.user)
    return render(request, "appointments/list.html", {"appointments": appointments})
