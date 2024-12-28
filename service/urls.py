
from django.contrib import admin
from django.urls import path, include
from service import views
from middlewares.admin_auth import admin_middleware

urlpatterns = [
    path('add_service/', admin_middleware(views.add_service), name='admin_panel.add_service'),
    path('add_service_info/', admin_middleware(views.add_service_info), name='admin_panel.add_service_info'),
    path('services/', admin_middleware(views.services), name='admin_panel.services'),
]
