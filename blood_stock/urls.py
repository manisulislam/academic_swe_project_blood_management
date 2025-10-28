from django.urls import path
from .views import stock_view, update_stock

urlpatterns = [
    path('blood_stock/', stock_view, name='view_stock'),
    path('update/', update_stock, name='update_stock'),
]
