from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
import sweetify

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            print("User created:", user)
            sweetify.success(request, 'You Registered Successfully. Please log in first.', icon='success')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['password']
        user = authenticate(request, username=u, password=p)
        if user:
            login(request, user)
            sweetify.success(request, 'You log In  Successfully.', icon='success')
            return redirect('home')
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    sweetify.success(request, 'You Log Out Successfully. Please log in first.', icon='success')
    return redirect('login')

def redirect_after_login(request):
    user = request.user
    if user.role == 'doctor':
        return redirect('doctor_dashboard')
    elif user.role == 'donor':
        return redirect('donor_dashboard')
    elif user.role == 'recipient':
        return redirect('recipient_dashboard')
    elif user.role == 'patient':
        return redirect('patient_dashboard')
    else:
        return redirect('home')