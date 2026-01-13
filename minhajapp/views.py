from django.http import JsonResponse # JSON রেসপন্সের জন্য
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout # নাম পরিবর্তন করা হয়েছে
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def profile(request):
    return render(request, 'profile.html')

def logout_view(request):
    logout(request)
    return redirect('login')

# ফাংশনের নাম login_view দিলে ভালো হয় কনফ্লিক্ট এড়াতে
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user) # এখানে auth_login ব্যবহার করা হয়েছে
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')

    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            # AJAX রিকোয়েস্ট হলে JSON এরর পাঠানো ভালো
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'status': 'error', 'message': 'Username already exists'})
            
            messages.error(request, 'Username already exists')
            return redirect('signup')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.save()

        # AJAX/Animation এর জন্য JSON রেসপন্স
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'status': 'success'})

        messages.success(request, 'Account created successfully')
        return redirect('login')

    return render(request, 'signup.html')

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard.html')