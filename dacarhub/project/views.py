from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.template import loader
from .models import car
from django.urls import reverse

# Create your views here.


# Create your views here.
def home(request):
    return render(request, 'index.html')


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def booking(request):
    return render(request, 'booking.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']


        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Your Credetials doesn't match!!!")
            return redirect('login')
    else:
        return render(request, 'login.html')


def service(request):
    return render(request, 'service.html')


def carview(request):
    vehicles = car.objects.all()
    context = {'vehicles' : vehicles}
    return render(request, 'car.html', context)


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Used email, please try another email.')
                return redirect ('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect ('login')
        else:
            messages.info(request, "Password doesn't match!" )
            return redirect ('register')
    else:
        return render(request, 'register.html')

