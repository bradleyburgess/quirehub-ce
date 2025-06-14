INSTALLED_APPS = (
    # 1. Django
    [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
    ]
    # 2. Third-party
    + [
        "allauth",
        "allauth.account",
        "crispy_forms",
        "crispy_bootstrap5",
    ]
    # 3. QuireHub
    + [
        "base",
        "users",
        "dashboard",
        "choirs",
    ]
)
