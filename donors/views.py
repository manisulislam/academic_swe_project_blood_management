from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import DonorProfile
from .forms import DonorProfileForm
from django.db.models import Sum

from blood_stock.models import BloodStock
from recipients.models import BloodRequest




@login_required
def user_profile(request):
    return render(request, 'core/profile.html', {'user': request.user})


def donor_list(request):
    # Fetch all donor profiles where the user has role='donor'
    donors = DonorProfile.objects.filter(user__role='donor')
    return render(request, 'donors/donor_list.html', {'donors': donors})


def donor_create(request):
    try:
        profile = request.user.donorprofile
        form = DonorProfileForm(instance=profile)
    except DonorProfile.DoesNotExist:
        form = DonorProfileForm()

    if request.method == "POST":
        try:
            profile = request.user.donorprofile
            form = DonorProfileForm(request.POST, instance=profile)
        except DonorProfile.DoesNotExist:
            form = DonorProfileForm(request.POST)

        if form.is_valid():
            donor_profile = form.save(commit=False)
            donor_profile.user = request.user  # set the user
            donor_profile.save()
            form.save_m2m()  # save many-to-many diseases
            return redirect('donor_list')  # change to your URL

    return render(request, 'donors/donor_create.html', {'form': form})

@login_required
def donor_update(request, pk):
    donor = get_object_or_404(DonorProfile, pk=pk)
    # Optional: Allow update only if the logged-in user owns this profile or is staff
    if request.user != donor.user and not request.user.is_staff:
        return redirect('donor_list')

    if request.method == 'POST':
        form = DonorProfileForm(request.POST, instance=donor)
        if form.is_valid():
            form.save()
            return redirect('donor_list')
    else:
        form = DonorProfileForm(instance=donor)
    return render(request, 'donors/donor_create.html', {'form': form})

@login_required
def donor_delete(request, pk):
    donor = get_object_or_404(DonorProfile, pk=pk)
    
    # Optional: Allow delete only if the logged-in user owns this profile or is staff
    if request.user != donor.user and not request.user.is_staff:
        return redirect('donor_list')

    if request.method == 'POST':
        # First delete the DonorProfile
        donor.delete()
        # Then delete the related user
        donor.user.delete()
        return redirect('donor_list')
    
    return render(request, 'donors/donor_confirm_delete.html', {'donor': donor})




def blood_chart_view(request):
    # Total units donated per blood group
    blood_stock = BloodStock.objects.all()
    blood_groups = [b.blood_group for b in blood_stock]
    donated_units = [b.units for b in blood_stock]

    # Total units requested per blood group
    requests = BloodRequest.objects.filter(status='approved')
    requested_units = []
    for bg in blood_groups:
        total = requests.filter(blood_group=bg).aggregate(Sum('units'))['units__sum'] or 0
        requested_units.append(total)

    context = {
        'blood_groups': blood_groups,
        'donated_units': donated_units,
        'requested_units': requested_units
    }
    return render(request, 'donors/blood_chart.html', context)
