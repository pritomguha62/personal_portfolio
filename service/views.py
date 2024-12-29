from django.shortcuts import render, redirect, get_object_or_404
from .models import *
import os
from django.http import HttpResponseRedirect
from django.contrib import messages

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

        messages.success(request, "Service added successfully.")

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def all_services(request):
    services = Service.objects.all()
    return render(request, 'admin_templates/services.html', {'services':services})


def delete_service(request, id):
    service = get_object_or_404(Service, id=id)
    if service.image and os.path.isfile(service.image.path):
        os.remove(service.image.path)
    service.delete()
    messages.success(request, "Service deleted successfully.")
    # return redirect('blog_post_detail', id=service.id)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

