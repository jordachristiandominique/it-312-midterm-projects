from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),        # Landing page
    path('home/', views.home, name='home'),     # Dashboard after login
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),

    # Project URLs
    path('projects/fun-facts-api/', views.fun_facts_api, name='fun_facts_api'),
    path('projects/scripting-automation/', views.scripting_automation, name='scripting_automation'),
    path('projects/login-otp-qr/', views.login_otp_qr, name='login_otp_qr'),
    path('projects/joke-encryption-qr/', views.joke_encryption_qr, name='joke_encryption_qr'),
    path('projects/security-programming/', views.security_programming, name='security_programming'),
    path('projects/api-design/', views.api_design, name='api_design'),
]