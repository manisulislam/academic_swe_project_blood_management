from django.urls import path
from . import views

urlpatterns = [
    path("medicines/", views.medicine_list, name="medicine_list"),
    path("order/<int:med_id>/", views.order_medicine, name="order_medicine"),
    path("orders/", views.my_orders, name="my_orders"),
]
