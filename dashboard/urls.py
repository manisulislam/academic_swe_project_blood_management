from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('donors/', views.donor_list, name='donors'),
    path('settings/', views.settings_view, name='settings'),  # ✅ Settings page
]
