from django.http import HttpResponse
from service.models import Service
from portfolio.models import Portfolio


from django.shortcuts import render

def home(request):

    services = Service.objects.all()

    portfolios = Portfolio.objects.all()

    return render(request, 'pub_templates/index.html', {'services':services, 'portfolios':portfolios})

