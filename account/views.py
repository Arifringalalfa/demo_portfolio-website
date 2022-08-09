from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def user_log(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User = authenticate(request, username=username, password=password)

        if User is not None:
            login(request, User)
            return redirect('home')

        else:
            print('User Not Found')
    return render(request, './auth/login.html')


def user_logOut(request):
    logout(request)
    return redirect('login')
