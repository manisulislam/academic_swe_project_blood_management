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
    announcements = Announcement.objects.all().order_by('-created_on')  # latest first
    return render(request, "core/list.html", {"announcements": announcements})

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



def faq_view(request):
    faqs = [
        {"q": "Who can donate blood?", "a": "Anyone aged 18–60 years, weighing at least 50 kg, and in good health can donate blood."},
        {"q": "How often can I donate blood?", "a": "Men: every 3 months, Women: every 4 months."},
        {"q": "Is blood donation safe?", "a": "Yes. Sterile and disposable equipment is used, and it does not affect your health."},
        {"q": "How much blood is taken during donation?", "a": "About 350–450 ml depending on body weight."},
        {"q": "Can I donate blood if I am taking medication?", "a": "Some medicines may temporarily defer you from donating. Always inform the doctor."},
        {"q": "Can I donate if I had COVID-19?", "a": "Yes, but only after 28 days of full recovery and being symptom-free."},
        {"q": "What should I do before and after donation?", "a": "Eat light, drink water, and rest shortly after donation."},
        {"q": "How do I request blood?", "a": "Submit a request form mentioning blood group, units, hospital, urgency, and reason."},
        {"q": "How long does it take to arrange blood?", "a": "It depends on donor availability and group compatibility. The system matches requests quickly."},
        {"q": "Do I need to pay for blood?", "a": "Donation is free, but hospitals may charge screening/service fees."},
        {"q": "Can I request a specific donor?", "a": "Yes, you can mention it, or the system finds the best available donor."},
        {"q": "How is blood safety ensured?", "a": "All blood is tested for HIV, Hepatitis B & C, Malaria, and Syphilis."},
        {"q": "Can blood be stored for later use?", "a": "Yes, whole blood can be stored 35–42 days depending on preservative."},
        {"q": "What if no donor is available?", "a": "The system notifies nearby donors immediately. Urgent requests are prioritized."},
    ]
    return render(request, "core/faq.html", {"faqs": faqs})

def privacy_policy(request):
    return render(request, "core/privacy_policy.html")



def terms_conditions(request):
    return render(request, "core/terms_conditions.html")