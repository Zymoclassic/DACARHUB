from django.urls import path
from . import views
from django.urls import reverse


urlpatterns = [
    path('', views.home, name='home'),
    path('index', views.index, name='index'),
    path('login', views.login, name='login'),
    path('service', views.service, name='service'),
    path('car', views.carview, name='car'),
    path('about', views.about, name='about'),
    path('booking', views.booking, name='booking'),
    path('register', views.register, name='register')
]