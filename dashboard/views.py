from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm



@login_required
def home(request):
    return render(request, 'dashboard/home.html')

@login_required
def profile(request):
    user = request.user  
    return render(request, 'dashboard/profile.html', {'user': user})
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'dashboard/edit_profile.html', {'form': form})
@login_required
def donor_list(request):
    # Replace with your actual queryset
    donors = []  
    return render(request, 'dashboard/donor_list.html', {'donors': donors})

@login_required
def settings_view(request):
    if request.method == "POST":
        # Handle form submission (e.g., update user info)
        pass
    return render(request, 'dashboard/settings.html')
