from typing import cast

from django import template
from django.http import HttpRequest
from django.template.context import Context

register = template.Library()


@register.simple_tag(takes_context=True)
def active_link(context: Context, app_section: str) -> str:
    request = cast(HttpRequest, context.get("request"))
    if request.path.startswith(f"/app/{app_section}"):
        return "active"
    return ""


@register.simple_tag(takes_context=True)
def aria_current_page(context: Context, app_section: str) -> str:
    request = cast(HttpRequest, context.get("request"))
    if request and request.path.startswith(f"/app/{app_section}"):
        return "aria-current=page"
    return ""
