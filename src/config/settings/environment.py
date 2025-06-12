import os
from pathlib import Path

import environ

env = environ.Env(
    DEBUG=(bool, False),
    PG_HOST=(str),
    PG_USER=(str),
    PG_DATABASE=(str),
    PG_PASSWORD=(str),
    PG_PORT=(int),
    DJANGO_SECRET_KEY=(str),
)

BASE_DIR = Path(__file__).resolve().parents[2]

environ.Env.read_env(os.path.join(Path(BASE_DIR).parent, ".env"))

DEBUG = env("DEBUG")
