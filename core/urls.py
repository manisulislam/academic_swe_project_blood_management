from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('announcement_list', views.announcement_list, name='announcement_list'),
    path('create/', views.announcement_create, name='announcement_create'),
    path('edit/<int:pk>/', views.announcement_update, name='announcement_update'),
    path('delete/<int:pk>/', views.announcement_delete, name='announcement_delete'),
    path('contact/', views.contact_us, name='contact_us'),
    path('about/', views.about, name='about'),
    path("faq/", views.faq_view, name="faq"),
    path("privacy-policy/", views.privacy_policy, name="privacy_policy"),
    path("terms-and-conditions/", views.terms_conditions, name="terms_conditions"),

    
]
