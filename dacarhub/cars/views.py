from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import car


def carview(request):
    vehicles = car.objects.all()
    context = {'vehicles' : vehicles}
    return render(request, 'car.html', context)


def booking(request):
    return render(request, 'booking.html')


