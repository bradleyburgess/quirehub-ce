from django.contrib.auth import authenticate, get_user_model, login
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from choirs.forms import ChoirCreateForm
from users.forms import AdminSignupForm

User = get_user_model()


def home_page(request: HttpRequest) -> HttpResponse:
    return render(request, "pages/home.html")


def initial_setup(request: HttpRequest) -> HttpResponse:
    admin_form = AdminSignupForm()
    choir_form = ChoirCreateForm()
    if request.method == "POST":
        _admin_form = {
            "first_name": request.POST["first_name"],
            "last_name": request.POST["last_name"],
            "email": request.POST["email"],
            "password1": request.POST["password1"],
            "password2": request.POST["password2"],
        }
        _choir_form = {
            "name": request.POST["name"],
            "description": request.POST["description"],
        }
        admin_form = AdminSignupForm(_admin_form)
        choir_form = ChoirCreateForm(_choir_form)
        if admin_form.is_valid() and choir_form.is_valid():
            user = User.objects.create_user(  # type: ignore
                email=admin_form.cleaned_data["email"],
                password=admin_form.cleaned_data["password1"],
            )
            user = authenticate(request, email=user.email, password=user.password)
            login(request, user)
            return redirect(reverse_lazy("pages.home"))
    return render(
        request,
        "pages/initial-setup.html",
        {"admin_form": admin_form, "choir_form": choir_form},
    )
