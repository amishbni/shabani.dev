from django.shortcuts import render
from .forms import UsernameForm

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

