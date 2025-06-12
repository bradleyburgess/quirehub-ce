from collections.abc import Callable

from django.core.cache import cache
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy

from choirs.models import Choir


class CheckForChoirMiddleware:
    def __init__(self, get_response: Callable[[HttpRequest], HttpResponse]):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        path = request.path
        if path.startswith("/admin/") or path.startswith("/static/"):
            return self.get_response(request)

        choir_exists = cache.get("choir_exists")
        if choir_exists is None:
            choir_exists = Choir.objects.exists()
            cache.set("choir_exists", choir_exists, timeout=60 * 5)

        if not choir_exists:
            if path.startswith("/initial-setup"):
                return self.get_response(request)
            return redirect(reverse_lazy("pages.initial-setup"))
        return self.get_response(request)
