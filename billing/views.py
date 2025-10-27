from django.shortcuts import render, redirect
from .models import Invoice
from django.contrib.auth.decorators import login_required

@login_required
def patient_invoices(request):
    invoices = Invoice.objects.filter(patient=request.user)
    return render(request, "billing/invoices.html", {"invoices": invoices})

@login_required
def pay_invoice(request, invoice_id):
    invoice = Invoice.objects.get(id=invoice_id)
    invoice.status = "Paid"
    invoice.save()
    return redirect("patient_invoices")
