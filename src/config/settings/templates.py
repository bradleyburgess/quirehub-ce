from .environment import BASE_DIR, DEBUG

TEMPLATE_CONTEXT_PROCESSORS = [
    "django.template.context_processors.request",
    "django.contrib.auth.context_processors.auth",
    "django.contrib.messages.context_processors.messages",
]

if DEBUG:
    TEMPLATE_CONTEXT_PROCESSORS.append("django.template.context_processors.debug")

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": TEMPLATE_CONTEXT_PROCESSORS,
        },
    },
]
