from django.shortcuts import render, redirect, get_object_or_404
from .models import Ambulance, AmbulanceRequest
from django.contrib.auth.decorators import login_required

@login_required
def request_ambulance(request):
    if request.method == "POST":
        pickup = request.POST.get("pickup")
        destination = request.POST.get("destination")
        AmbulanceRequest.objects.create(
            user=request.user,
            pickup_location=pickup,
            destination=destination,
        )
        return redirect("ambulance_success")
    return render(request, "ambulance/request_form.html")

@login_required
def ambulance_list(request):
    ambulances = Ambulance.objects.all()
    return render(request, "ambulance/list.html", {"ambulances": ambulances})
