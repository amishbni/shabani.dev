from django.shortcuts import render
from .forms import UsernameForm

def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def statsfm_view(request, *args, **kwargs):
    if request.method == "GET":
        form = UsernameForm(request.GET)
    else:
        form = UsernameForm()

    return render(request, "statsfm.html", {'form': form})

