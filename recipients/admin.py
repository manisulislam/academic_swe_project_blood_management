from django.contrib import admin
from .models import BloodRequest
from blood_stock.models import BloodStock
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


# BloodRequest admin
@admin.register(BloodRequest)
class BloodRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'blood_group', 'units', 'hospital', 'urgency', 'status', 'requested_on')
    list_filter = ('status', 'blood_group', 'urgency')
    search_fields = ('user__username', 'blood_group', 'hospital')
    actions = ['approve_request', 'reject_request']

    # Approve selected blood requests
    def approve_request(self, request, queryset):
        for br in queryset:
            try:
                stock = BloodStock.objects.get(blood_group=br.blood_group)
            except BloodStock.DoesNotExist:
                stock = None

            if stock and stock.units >= br.units:
                # Update request and stock
                br.status = 'approved'
                stock.units -= br.units
                stock.save()
                br.save()

                # Send email to user
                mail_subject = "Blood Request Approved ✅"
                message = render_to_string(
                    "recipients/blood_collected_mail.html",
                    {
                        'user': br.user,
                        'blood_group': br.blood_group,
                        'units': br.units,
                        'hospital': br.hospital,
                        'urgency': br.urgency,
                        'request_date': br.request_date,
                        'request_time': br.request_time,
                        'reason': br.reason,
                        'requested_on': br.requested_on,
                    }
                )
                send_email = EmailMultiAlternatives(mail_subject, '', to=[br.user.email])
                send_email.attach_alternative(message, 'text/html')
                send_email.send()

        self.message_user(request, "Selected requests have been approved (if enough stock).")
    approve_request.short_description = "Approve selected requests"

    # Reject selected blood requests
    def reject_request(self, request, queryset):
        for br in queryset:
            br.status = 'rejected'
            br.save()

            # Send rejection email
            mail_subject = "Blood Request Rejected ❌"
            message = render_to_string(
                "recipients/blood_rejected_mail.html",
                {
                    'user': br.user,
                    'blood_group': br.blood_group,
                    'units': br.units,
                    'hospital': br.hospital,
                    'urgency': br.urgency,
                    'request_date': br.request_date,
                    'request_time': br.request_time,
                    'reason': br.reason,
                    'requested_on': br.requested_on,
                }
            )
            send_email = EmailMultiAlternatives(mail_subject, '', to=[br.user.email])
            send_email.attach_alternative(message, 'text/html')
            send_email.send()

        self.message_user(request, "Selected requests have been rejected.")
    reject_request.short_description = "Reject selected requests"
