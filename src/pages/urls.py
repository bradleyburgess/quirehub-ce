from django.urls import path

from . import views

app_name = "pages"

urlpatterns = [
    path("", views.index_page, name="index"),
    path("initial-setup", views.initial_setup, name="initial-setup"),
]
