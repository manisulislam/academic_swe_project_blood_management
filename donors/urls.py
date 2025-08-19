from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.user_profile, name='user_profile'),
    path('donors/', views.donor_list, name='donor_list'),
    path('donors/create/', views.donor_create, name='donor_create'),
    path('donors/<int:pk>/edit/', views.donor_update, name='donor_update'),
    path('donors/<int:pk>/delete/', views.donor_delete, name='donor_delete'),
    path('blood-chart/', views.blood_chart_view, name='blood_chart'),
]
