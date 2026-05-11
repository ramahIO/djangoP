from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm  = request.POST.get('confirm')

        if password != confirm:
            messages.error(request, 'Passwords do not match!')
            return redirect('/users/register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            return redirect('/users/register')

        User.objects.create_user(username=username, password=password)
        messages.success(request, 'Registered successfully!')
        return redirect('/users/login')

    return render(request, 'usermodule/register.html')


from django.contrib.auth import login, authenticate

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successfully!')
            return redirect('/')
        else:
            messages.error(request, 'Invalid username or password!')
            return redirect('/users/login')

    return render(request, 'usermodule/login.html')



from django.contrib.auth import login, authenticate, logout

def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('/users/login')