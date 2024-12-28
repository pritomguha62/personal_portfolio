from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def add_service(request):
    return render(request, 'admin_templates/add_service.html')

def add_service_info(request):
    
    if request.method == "POST":
        
        service_info = request.POST
        
        title = service_info.get('title')
        short_description = service_info.get('short_description')
        description = service_info.get('description')
        image = request.FILES.get('image')
        
        Service.objects.create(
            title = title,
            short_description = short_description,
            description = description,
            image = image,
        )
        
        return redirect('home')

def services(request):
    services = Service.objects.all()
    return render(request, 'admin_templates/services.html', {'services':services})
