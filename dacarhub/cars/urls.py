from django.urls import path
from . import views


urlpatterns = [
    path('', views.carview, name='car'),
    #path('booking/<car.name>', views.booking, name='booking'),
]

