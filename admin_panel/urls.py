
from django.contrib import admin
from django.urls import path, include
from admin_panel import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('service/', include("service.urls")),
    path('dashboard', views.dashboard),
]
