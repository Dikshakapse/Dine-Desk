from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.timezone import now
from menu.models import DailyMenu
from orders.models import Order


def homepage(request):
    return render(request, 'home.html')

def aboutpage(request):
    return render(request, 'about.html')

def registerpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('register')

        # Create user but DO NOT auto-login
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()

        # Use custom flag to show success message in template
        return render(request, 'register.html', {'registered': True, 'username': username})

    return render(request, 'register.html')

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('order')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    messages.info(request, "You've been logged out.")
    return redirect('home')


@login_required(login_url='login')
def order_view(request):
    today = now().date()
    menu_items = DailyMenu.objects.filter(available_on=today)
    return render(request, 'order.html', {'menu_items': menu_items})
