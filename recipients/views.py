from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import BloodRequest

@login_required
def request_blood(request):
    if request.method == 'POST':
        Bg = request.POST['blood_group']
        u = request.POST['units']
        BloodRequest.objects.create(user=request.user, blood_group=Bg, units=u)
        return redirect('request_history')
    return render(request, 'recipients/request_blood.html')

@login_required
def request_history(request):
    history = BloodRequest.objects.filter(user=request.user)
    return render(request, 'recipients/request_history.html', {'history': history})
