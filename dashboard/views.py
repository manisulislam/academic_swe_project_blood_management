from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'dashboard/home.html')

@login_required
def profile(request):
    return render(request, 'dashboard/profile.html')

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
