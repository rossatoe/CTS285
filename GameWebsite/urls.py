from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from home import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('account-profile/', views.account_profile, name='account_profile'),
    path('account-registration/', views.account_register, name='account_register'),
    path('account-login/', views.account_login, name='account_login'),
    path('account-verification/', views.account_verify, name='account_verify'),
    path('reset_verification/', views.reset_verification, name='reset_verification'),
    path('account-profile/edit/', views.account_profile_edit, name='account_profile_edit'),
    path('account-logout/', LogoutView.as_view(), name='account_logout'),
]

# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    # Serve media files (if needed)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
