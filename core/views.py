from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.timezone import now
from .models import Announcement
from .forms import AnnouncementForm 
from blood_stock.forms import ContactForm
from django.db.models import Q 
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm
from django.utils import timezone

def home(request):
    return render(request, 'core/home.html')

def announcement_list(request):
    
    announcements = Announcement.objects.all()

def announcement_create(request):
    if request.method == 'POST':
        form = AnnouncementForm(request.POST, request.FILES)
        if form.is_valid():
            announcement = form.save(commit=False)
            announcement.author = request.user
            announcement.save()
            return redirect('announcement_list')
    else:
        form = AnnouncementForm()
    return render(request, 'core/annouce_form.html', {'form': form, 'title': 'Create Announcement'})

@login_required

def announcement_update(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk)
    if request.method == 'POST':
        form = AnnouncementForm(request.POST, request.FILES, instance=announcement)
        if form.is_valid():
            form.save()
            return redirect('announcement_list')
    else:
        form = AnnouncementForm(instance=announcement)
    return render(request, 'core/annouce_form.html', {'form': form, 'title': 'Edit Announcement'})

@login_required

def announcement_delete(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk)
    if request.method == 'POST':
        announcement.delete()
        return redirect('announcement_list')
    return render(request, 'core/confirm_delete.html', {'announcement': announcement})


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for contacting us. We'll get back to you soon!")
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'core/contact_us.html', {'form': form})

def about(request):
    return render(request, 'core/about.html')