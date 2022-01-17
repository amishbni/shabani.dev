from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import (
    AuthenticationForm
)
from .forms import UsernameForm


def login_view(request, *args, **kwargs):
    if request.user.is_authenticated:
        return redirect("demo")

    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(
                username=username,
                password=password
            )
            if user:
                login(request, user)
                return redirect("demo")

    context = {"form": form}
    return render(request, "login_register.html", context)


def logout_view(request, *args, **kwargs):
    logout(request)
    return redirect("demo")


def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})


def statsfm_view(request, *args, **kwargs):
    if request.method == "GET":
        form = UsernameForm(request.GET)
        if form.is_valid():
            username = form.cleaned_data["username"]
    else:
        form = UsernameForm()

    context = {
        "form": form,
        "username": username,
    }

    return render(request, "statsfm.html", context)


def demo_view(request, *args, **kwargs):
    context = {}
    return render(request, "demo.html", context)

