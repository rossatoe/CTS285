# urls.py
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('account-registration/', views.account_register, name='account_register'),
    path('account-login/', views.account_login, name='account_login'),
    path('account-verification/', views.account_verify, name='account_verify'),
    path('reset-verification/', views.reset_verification, name='reset_verification'),
    path('account-profile/', views.account_profile, name='account_profile'),
    path('account-profile/edit/', views.account_profile_edit, name='account_profile_edit'),
    path('account-logout/', LogoutView.as_view(), name='account_logout'),  # Logout URL
]