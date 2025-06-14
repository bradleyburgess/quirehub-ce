from django.template import Context
from django.test import RequestFactory

from base.templatetags.active_page import active_link, aria_current_page


class TestActiveLinkTemplateTag:
    def test_returns_active(self):
        factory = RequestFactory()
        request = factory.get("/app/dashboard")
        result = active_link(Context({"request": request}), "dashboard")
        assert result == "active"

    def test_returns_blank(self):
        factory = RequestFactory()
        request = factory.get("/app/dashboard")
        result = active_link(Context({"request": request}), "events")
        assert result == ""

    def test_returns_blank_not_app(self):
        factory = RequestFactory()
        request = factory.get("/dashboard")
        result = active_link(Context({"request": request}), "dashboard")
        assert result == ""


class TestAriaCurrentPageTemplateTag:
    def test_returns_aria_current(self):
        factory = RequestFactory()
        request = factory.get("/app/dashboard")
        result = aria_current_page(Context({"request": request}), "dashboard")
        assert result == "aria-current=page"

    def test_returns_blank(self):
        factory = RequestFactory()
        request = factory.get("/app/dashboard")
        result = aria_current_page(Context({"request": request}), "events")
        assert result == ""
