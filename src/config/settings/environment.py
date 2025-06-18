import os
from pathlib import Path

from environ import environ

env = environ.Env(
    DEBUG=(bool, True),
    SECRET_KEY=(str),
)


BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

DEBUG = env("DEBUG")
