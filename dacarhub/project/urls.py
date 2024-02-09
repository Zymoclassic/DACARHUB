from django.urls import path
from . import views
from django.urls import reverse


urlpatterns = [
    path('', views.home, name='home'),
    path('index', views.index, name='index'),
    path('service', views.service, name='service'),
    path('about', views.about, name='about'),
]

