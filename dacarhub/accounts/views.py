from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


def accounts(request):
    return render(request, 'accounts.html')


def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists, please try another username.')
                return redirect ('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Used email, please try another email.')
                return redirect ('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect ('login')
        else:
            messages.info(request, "Password doesn't match!" )
            return redirect ('register')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Your credentials doesn't match!!!")
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('index')