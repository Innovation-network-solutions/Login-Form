from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'app/home.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')

        if password1 != password2:
            return HttpResponse('Your username and password are not same!!!')
        else:

            my_user = User.objects.create_user(username, email, password1)
            my_user.save()
            return redirect('login')
    return render(request, 'app/signup.html')


def my_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse('Username or Password is incorrect!!!')
        else:
            return redirect('home')

    return render(request, 'app/index.html')


def logout(request):
    auth.logout(request)
    return redirect('login')
