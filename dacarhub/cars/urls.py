from django.urls import path
from . import views


urlpatterns = [
    path('', views.carview, name='car'),
    path('booking/<str:vehiclename>', views.booking, name='booking'),
]

