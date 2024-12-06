
from django.contrib import admin
from django.urls import path, include
from admin_panel import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('service/', include("service.urls")),
    path('', views.dashboard),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('signin/', views.signin, name='admin_panel.signin'),
    path('signup/', views.signup, name='admin_panel.signup'),
    path('signin_info/', views.signin, name='admin_panel.signin_info'),
    path('signup_info/', views.signup, name='admin_panel.signup_info'),
]
