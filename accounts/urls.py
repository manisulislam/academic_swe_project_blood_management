from django.urls import path
from .views import register_view, login_view, logout_view,redirect_after_login

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('redirect-after-login/', redirect_after_login, name='redirect_after_login'),
]
