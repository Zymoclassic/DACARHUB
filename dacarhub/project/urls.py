from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('service/', views.service, name='service'),
    path('car/', views.car, name='car'),
    path('about/', views.about, name='about'),
    path('booking/', views.booking, name='booking'),
    path('register/', views.register, name='register')
]