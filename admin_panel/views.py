from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from django.contrib.auth.models import User

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

        return HttpResponse(request.POST.get('email') + request.POST.get('password'))

def signup_info(request):

    if request.method == "POST":

        if request.POST.get('terms_privacy') != 'on':

            previous_url = request.META.get('HTTP_REFERER', '/')

            return redirect(previous_url)

        name = request.POST.get('name')

        email = request.POST.get('email')

        password = request.POST.get('password')

        User.objects.create(
            name = name,
            email = name,
        )

        User.set_password(password)
        User.save()

        return HttpResponse(request.POST.get('email') + request.POST.get('password'))

