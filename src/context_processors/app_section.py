from django.http import HttpRequest


def app_section(request: HttpRequest):
    has_app = request.path.startswith("/app/")
    if has_app:
        return {"app_section": request.path.split("/")[2]}
    return {}
