from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('accounts/', include('accounts.urls')),
    path('donors/', include('donors.urls')),
    path('recipients/', include('recipients.urls')),
    path('stock/', include('blood_stock.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('ambulance/', include('ambulance.urls')),
    path('appointments/', include('appointments.urls')),
]