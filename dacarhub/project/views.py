from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import loader
from .models import car

# Create your views here.


# Create your views here.
def home(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())


def booking(request):
    template = loader.get_template('booking.html')
    return HttpResponse(template.render())


def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())


def service(request):
    template = loader.get_template('service.html')
    return HttpResponse(template.render())


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

