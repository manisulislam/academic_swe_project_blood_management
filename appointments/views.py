from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model
from .models import Appointment

User = get_user_model()


@login_required
def create_appointment(request):
    # Get all doctors to show in the dropdown
    doctors = User.objects.filter(role="doctor")

    if request.method == "POST":
        doctor_id = request.POST.get("doctor")
        date = request.POST.get("date")
        time = request.POST.get("time")

        # Validate doctor selection
        if not doctor_id:
            messages.error(request, "Please select a doctor.")
            return redirect("create_appointment")

        try:
            doctor = User.objects.get(id=doctor_id, role="doctor")
        except User.DoesNotExist:
            messages.error(request, "Invalid doctor selected.")
            return redirect("create_appointment")

        # Create appointment
        Appointment.objects.create(
            doctor=doctor,
            patient=request.user,
            date=date,
            time=time
        )

        messages.success(request, "Appointment created successfully!")
        return redirect("appointment_list")

    return render(request, "appointments/create.html", {"doctors": doctors})


@login_required
def appointment_list(request):
    # Filter based on role
    if request.user.role == "doctor":
        appointments = Appointment.objects.filter(doctor=request.user)
    else:
        appointments = Appointment.objects.filter(patient=request.user)

    return render(request, "appointments/list.html", {
        "appointments": appointments
    })
