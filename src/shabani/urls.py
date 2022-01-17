from django.contrib import admin
from django.urls import path
from django.conf import settings
from pages import views

urlpatterns = [
    path("", views.home_view),
    path("statsfm", views.statsfm_view),
    path("demo", views.demo_view, name="demo"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
]

if settings.ADMIN_ENABLED:
    urlpatterns.append(path("admin/", admin.site.urls))

