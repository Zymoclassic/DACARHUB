from django.shortcuts import render, redirect


def home(request):
    return render(request, 'index.html')


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def service(request):
    return render(request, 'service.html')


