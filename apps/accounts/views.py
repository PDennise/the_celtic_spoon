from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm  # Built-in Django login form
from django.contrib.auth import login, logout  # Functions to log users in and out
from django.contrib import messages  # Django's built-in messaging framework
from .forms import ARegistrationForm  # Custom user registration form


# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = ARegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully!")
            return redirect("/")
        messages.error(request, "Please correct the errors below.")
    else:
        form = ARegistrationForm()
    return render(request, "accounts/register.html", {"form": form})


def login_view(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect("/")
        messages.error(request, "Invalid username or password")
    return render(request, "accounts/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("/")
