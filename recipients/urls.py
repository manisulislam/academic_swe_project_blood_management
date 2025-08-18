from django.urls import path
from .views import request_blood, request_history

urlpatterns = [
    path('make/', request_blood, name='make_request'),
    path('history/', request_history, name='request_history'),
]
