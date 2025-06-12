from django.urls import path

from . import views

urlpatterns = [
    path("", views.home_page, name="pages.home"),
    path("initial-setup", views.initial_setup, name="pages.initial-setup"),
]
