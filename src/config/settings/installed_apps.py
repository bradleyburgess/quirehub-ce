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
    ]
    # 3. QuireHub
    + [
        "users",
        "choirs",
    ]
)
