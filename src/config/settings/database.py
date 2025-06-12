import os
from pathlib import Path

from .environment import BASE_DIR, DEBUG, env

if DEBUG:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(Path(BASE_DIR).parent, "db.sqlite3"),
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "HOST": env("PG_HOST"),
            "USER": env("PG_USER"),
            "NAME": env("PG_DATABASE"),
            "PASSWORD": env("PG_PASSWORD"),
            "PORT": env("PG_PORT"),
        }
    }

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
