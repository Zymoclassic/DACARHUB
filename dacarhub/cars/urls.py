from django.urls import path
from . import views
from django.urls import reverse


urlpatterns = [
    path('car', views.carview, name='car'),
    path('booking', views.booking, name='booking'),
]

