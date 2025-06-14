from django.contrib.auth import get_user_model, login
from django.core.cache import cache
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from choirs.forms import ChoirCreateForm
from choirs.models import Choir
from users.forms import AdminSignupForm

User = get_user_model()


def index_page(request: HttpRequest) -> HttpResponse:
    return render(request, "pages/home.html")


def initial_setup(request: HttpRequest) -> HttpResponse:
    choir_exists = cache.get("choir_exists")
    if choir_exists:
        if request.method == "POST":
            return HttpResponseBadRequest("Choir already exists")
        return redirect(reverse_lazy("pages:index"))
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
            user = User.objects.create_superuser(  # type: ignore
                email=admin_form.cleaned_data["email"],
                password=admin_form.cleaned_data["password1"],
                first_name=admin_form.cleaned_data["first_name"],
                last_name=admin_form.cleaned_data["last_name"],
            )
            login(request, user, backend="django.contrib.auth.backends.ModelBackend")
            Choir.objects.create(
                name=choir_form.cleaned_data["name"],
                description=choir_form.cleaned_data["description"],
                created_by=user,
            )
            cache.set("choir_exists", True)
            return redirect(reverse_lazy("dashboard:index"))
    return render(
        request,
        "pages/initial-setup.html",
        {"admin_form": admin_form, "choir_form": choir_form},
    )
