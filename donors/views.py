from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import DonorProfile
from .forms import DonorProfileForm

@login_required
def user_profile(request):
    return render(request, 'core/profile.html', {'user': request.user})



def donor_list(request):
    donors = DonorProfile.objects.all()
    return render(request, 'donors/donor_list.html', {'donors': donors})


def donor_create(request):
    # If user already has a profile, redirect to edit page
    if DonorProfile.objects.filter(user=request.user).exists():
        donor = DonorProfile.objects.get(user=request.user)
        return redirect('donor_update', pk=donor.pk)
    return redirect('register')
    # if request.method == 'POST':
    #     form = DonorProfileForm(request.POST)
    #     if form.is_valid():
    #         donor_profile = form.save(commit=False)
    #         donor_profile.user = request.user
    #         donor_profile.save()
    #         return redirect('donor_list')
    # else:
    #     form = DonorProfileForm()
    # return render(request, 'donors/donor_form.html', {'form': form})

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
    return render(request, 'donors/donor_form.html', {'form': form})

@login_required
def donor_delete(request, pk):
    donor = get_object_or_404(DonorProfile, pk=pk)
    # Optional: Allow delete only if the logged-in user owns this profile or is staff
    if request.user != donor.user and not request.user.is_staff:
        return redirect('donor_list')

    if request.method == 'POST':
        donor.delete()
        return redirect('donor_list')
    return render(request, 'donors/donor_confirm_delete.html', {'donor': donor})
