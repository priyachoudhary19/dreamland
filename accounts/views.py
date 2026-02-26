from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout 
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

#registration


def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # Check if already exists in Django User
        if User.objects.filter(username=email).exists():
            return render(request, 'register.html',
                          {'error': 'Email already registered'})

        # ✅ Create Django Auth User (IMPORTANT)
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password
        )

        # ✅ Save extra details in your custom table
        obj = registration()
        obj.name = request.POST['name']
        obj.email = email
        obj.mobile = request.POST['mobile']
        obj.password = password   # optional (but not recommended to store)
        obj.address = request.POST['address']
        obj.state = request.POST['state']
        obj.city = request.POST['city']
        obj.pincode = request.POST['pincode']
        obj.save()

        return redirect('login')

    return render(request, 'register.html')
    
#login

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, username=email, password=password)

        if user:
            login(request, user)
            return redirect("/packages/")   # 🔥 direct URL

        else:
            return render(request, "login.html", {"error": "Invalid Credentials"})

    return render(request, "login.html")

#home

def home(request):
    return render(request, "home.html")

#packages

@login_required(login_url='/login/')
def packages(request):
    return render(request, "packages.html")

#logout

def logout_view(request):
    logout(request)
    return redirect('home')   # logout ke baad home page