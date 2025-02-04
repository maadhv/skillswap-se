from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email already exists...")
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken...")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, "Account created successfully! You can now log in.")
                return redirect('explore')
        else:
            messages.error(request, "Passwords do not match...")
            return redirect('register')

    return render(request, 'register.html')
