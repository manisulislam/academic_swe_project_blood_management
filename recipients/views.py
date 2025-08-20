from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import BloodRequest
from .forms import BloodRequestForm
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
import sweetify
from blood_stock.models import BloodStock
from donors.models import DonorProfile  # DonorProfile import korte hobe


@login_required
def request_blood(request):
    if request.method == 'POST':
        form = BloodRequestForm(request.POST)
        if form.is_valid():
            blood_request = form.save(commit=False)
            blood_request.user = request.user

            # Check stock availability
            try:
                stock = BloodStock.objects.get(blood_group=blood_request.blood_group)
            except BloodStock.DoesNotExist:
                stock = None

            if stock and stock.units >= blood_request.units:
                # ✅ Stock available → Approve request
                blood_request.status = 'approved'
                stock.units -= blood_request.units
                stock.save()
                blood_request.save()

                sweetify.success(
                    request,
                    'Blood approved successfully. Our team will provide blood at that location',
                    icon='success'
                )

                # Send confirmation email to recipient
                mail_subject = 'Blood Request Submitted'
                message = render_to_string('recipients/request_blood_mail.html', {
                    'user': request.user,
                    'blood_group': blood_request.blood_group,
                    'units': blood_request.units,
                    'hospital': blood_request.hospital,
                    'urgency': blood_request.urgency,
                    'request_date': blood_request.request_date,
                    'request_time': blood_request.request_time,
                    'reason': blood_request.reason,
                    'status': blood_request.status,
                    'requested_on': blood_request.requested_on,
                })
                send_email = EmailMultiAlternatives(mail_subject, '', to=[request.user.email])
                send_email.attach_alternative(message, 'text/html')
                send_email.send()

            else:
                # ❌ Not enough stock → Pending
                blood_request.status = 'pending'
                blood_request.save()

                sweetify.success(
                    request,
                    'Blood request pending. Not enough stock. Our team will collect this blood.',
                    icon='warning'
                )

                # 🔔 Notify all donors of this blood group
                donor_emails = DonorProfile.objects.filter(
                    blood_group=blood_request.blood_group,
                    eligible_for_donation=True
                ).values_list("user__email", flat=True)

                donor_emails = list(filter(None, donor_emails))  # remove empty emails

                if donor_emails:
                    mail_subject = "Urgent Blood Donation Needed!"
                    message = render_to_string('donors/urgent_request_mail.html', {
                        'blood_group': blood_request.blood_group,
                        'units': blood_request.units,
                        'hospital': blood_request.hospital,
                        'urgency': blood_request.urgency,
                        'reason': blood_request.reason,
                    })
                    send_email = EmailMultiAlternatives(mail_subject, '', to=donor_emails)
                    send_email.attach_alternative(message, 'text/html')
                    send_email.send()

            return redirect('request_history')
    else:
        form = BloodRequestForm()

    return render(request, 'recipients/request_blood.html', {'form': form})


@login_required
def request_history(request):
    history = BloodRequest.objects.filter(user=request.user)
    return render(request, 'recipients/request_history.html', {'history': history})
