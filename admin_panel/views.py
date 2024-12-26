from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegistrationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import *
from django.contrib.auth import get_user_model

# User = get_user_model()

# Create your views here.

def dashboard(request):
    return render(request, 'admin_templates/dashboard.html')

def signin(request):
    return render(request, 'admin_templates/admin_signin.html')

def signup(request):
    return render(request, 'admin_templates/admin_signup.html')

def signin_info(request):

    if request.method == "POST":

        email = request.POST.get('email')

        password = request.POST.get('password')

        user = authenticate(email=email, password=password)

        if user is not None:
            login(request, user)

            # Set custom session data
            request.session['email'] = user.email
            request.session['is_admin'] = user.is_staff

            # return HttpResponse(user.is_staff)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password.")


def signup_info(request):

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)  # Log the user in after registration
            return redirect('home')  # Replace 'home' with your desired redirect URL
    else:
        form = UserRegistrationForm()
    return render(request, 'admin_templates/admin_signup.html', {'form': form})

def sign_out(request):
    # Log out the user
    logout(request)
    # Destroy the session completely
    request.session.flush()
    # Redirect to a specific page
    return redirect('home')

