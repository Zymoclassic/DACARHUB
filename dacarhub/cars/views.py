from django.shortcuts import render, redirect
from .models import car



def carview(request):
    vehicles = car.objects.all()
    context = {'vehicles' : vehicles}
    return render(request, 'car.html', context)


def booking(request, vehiclename):
    vehicle = car.objects.get(name=vehiclename)
    context = {'vehicle' : vehicle}
    return render(request, 'booking.html', context)


