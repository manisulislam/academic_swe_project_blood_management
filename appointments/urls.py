from django.urls import path
from . import views

urlpatterns = [
    path("new/", views.create_appointment, name="create_appointment"),
    path("list/", views.appointment_list, name="appointment_list"),
]
