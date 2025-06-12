from .environment import DEBUG, env

if DEBUG:
    SECRET_KEY = "django-insecure-key-afbdff015da17b7f0fc8d39f559133bb30e118050563301c"
else:
    SECRET_KEY = env("DJANGO_SECRET_KEY")

if DEBUG:
    INTERNAL_IPS = ["127.0.0.1", "localhost"]
