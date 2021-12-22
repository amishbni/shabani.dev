from django.shortcuts import render

def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def statsfm_view(request, *args, **kwargs):
    return render(request, "statsfm.html", {})

