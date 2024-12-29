
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
import os
from django.http import HttpResponseRedirect
from django.contrib import messages


# Create your views here.

def add_portfolio(request):
    services = Service.objects.all()
    return render(request, 'admin_templates/add_portfolio.html', {'services': services})


def add_portfolio_info(request):
    if request.method == "POST":
        portfolio_info = request.POST

        title = portfolio_info.get('title')
        short_description = portfolio_info.get('short_description')
        description = portfolio_info.get('description')
        image = request.FILES.get('image')
        service_id = request.POST.get("service")
        service = Service.objects.get(id=service_id)
        link = portfolio_info.get('link')

        Portfolio.objects.create(
            title=title,
            short_description=short_description,
            description=description,
            image=image,
            service=service,
            link=link,
        )

        messages.success(request, "Portfolio added successfully.")

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def all_portfolios(request):
    services = Service.objects.all()
    return render(request, 'admin_templates/services.html', {'services': services})


def delete_portfolio(request, id):
    service = get_object_or_404(Service, id=id)
    if service.image and os.path.isfile(service.image.path):
        os.remove(service.image.path)
    service.delete()
    messages.success(request, "Service deleted successfully.")
    # return redirect('blog_post_detail', id=service.id)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
