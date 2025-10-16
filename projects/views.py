from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def index(request):
    """Your existing landing page - untouched"""
    return render(request, 'index.html')

@login_required
def home(request):
    """Dashboard after login - shows all projects and user profile"""
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            # Fix: Use filter().first() instead of get() to handle multiple users
            user = User.objects.filter(email=email).first()
            if user:
                user = authenticate(request, username=user.username, password=password)
                if user:
                    login(request, user)
                    messages.success(request, f'Welcome back, {user.first_name}!')
                    return redirect('home')
                else:
                    messages.error(request, 'Invalid email or password')
            else:
                messages.error(request, 'No account found with this email')
        except Exception as e:
            messages.error(request, 'Login error occurred. Please try again.')
    
    return render(request, 'auth/login.html')

def register_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'An account with this email already exists')
        else:
            user = User.objects.create_user(
                username=email,  # Using email as username
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            messages.success(request, f'Welcome to IT-312 Projects, {first_name}!')
            user = authenticate(request, username=email, password=password)
            login(request, user)
            return redirect('home')
    
    return render(request, 'auth/register.html')

def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out successfully')
    return redirect('index')  # → Back to landing page

# Project Views
@login_required
def fun_facts_api(request):
    """Project 1: Fun Facts API - Simple system that calls any API"""
    return render(request, 'projects/fun_facts_api.html')

@login_required
def scripting_automation(request):
    """Project 2: Scripting Exercise - Automation with Fun Fact API email scheduling"""
    return render(request, 'projects/scripting_automation.html')

@login_required
def login_otp_qr(request):
    """Project 3: Login OTP and QR Code - Google Authenticator integration with joke API"""
    return render(request, 'projects/login_otp_qr.html')

@login_required
def joke_encryption_qr(request):
    """Project 4: Joke API Encryption QR Code - ATBASH, Caesar, Vigenere encryption with QR codes"""
    return render(request, 'projects/joke_encryption_qr.html')

@login_required
def security_programming(request):
    """Project 5: Application Security Programming - Encryption/Decryption cipher applications"""
    return render(request, 'projects/security_programming.html')

@login_required
def api_design(request):
    """Project 6: API Design - Django API documentation"""
    return render(request, 'projects/api_design.html')