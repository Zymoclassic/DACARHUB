from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import car

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
    template = loader.get_template('register.html')
    return HttpResponse(template.render())
