from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("pages.urls", namespace="pages")),
    path("app/dashboard/", include("dashboard.urls", namespace="dashboard")),
    path("accounts/", include("allauth.urls")),
]
