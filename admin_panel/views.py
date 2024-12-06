from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, 'admin_templates/dashboard.html')

def signin(request):
    return render(request, 'admin_templates/admin_signin.html')

def signup(request):
    return render(request, 'admin_templates/admin_signup.html')

def signin_info(request):
    return render(request, 'admin_templates/admin_signin.html')

def signup(request):
    return render(request, 'admin_templates/admin_signup.html')
