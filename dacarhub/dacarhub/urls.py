from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('project.urls')),
    path('index', include('project.urls')),
    path('about', include('project.urls')),
    path('service', include('project.urls')),
    path('car', include('cars.urls')),
    path('car/booking', include('cars.urls')),
    path('accounts', include('accounts.urls')),
    path('accounts/login', include('accounts.urls')),
    path('account/register', include('accounts.urls')),
    path('accounts/logout', include('accounts.urls')),
]
