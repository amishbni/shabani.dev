from django.contrib import admin
from django.urls import path
from django.conf import settings
from pages import views

urlpatterns = [
    path("", views.home_view),
    path("statsfm", views.statsfm_view),
]

if settings.ADMIN_ENABLED:
    urlpatterns.append(path("admin/", admin.site.urls))

