from django.urls import path
from . import views

urlpatterns = [
    path("request/", views.request_ambulance, name="request_ambulance"),
    path("list/", views.ambulance_list, name="ambulance_list"),
]
