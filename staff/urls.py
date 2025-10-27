from django.urls import path
from .views import (
    StaffListView,
    StaffDetailView,
    StaffCreateView,
    StaffUpdateView,
    StaffDeleteView,
)

urlpatterns = [
    path('staff/', StaffListView.as_view(), name='staff_list'),
    path('staff/<int:pk>/', StaffDetailView.as_view(), name='staff_detail'),
    path('staff/add/', StaffCreateView.as_view(), name='staff_add'),
    path('staff/<int:pk>/edit/', StaffUpdateView.as_view(), name='staff_edit'),
    path('staff/<int:pk>/delete/', StaffDeleteView.as_view(), name='staff_delete'),
]
