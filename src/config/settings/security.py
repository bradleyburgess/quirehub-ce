from .environment import DEBUG, env

if DEBUG:
    SECRET_KEY = "django-insecure-@+z@y3^r7fv@b*c38$&0=#a^$+&pug@og_#d*6upl(8-(k7^$i"
else:
    SECRET_KEY = env("SECRET_KEY")
    if not SECRET_KEY:
        raise ValueError("`SECRET_KEY` is not set!!")
