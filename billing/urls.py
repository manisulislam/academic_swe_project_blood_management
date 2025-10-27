from django.urls import path
from . import views

urlpatterns = [
    path("invoices/", views.patient_invoices, name="patient_invoices"),
    path("pay/<int:invoice_id>/", views.pay_invoice, name="pay_invoice"),
]
