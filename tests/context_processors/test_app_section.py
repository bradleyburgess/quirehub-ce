from django.test import RequestFactory

from context_processors import app_section


class TestAppSectionContextProcessor:
    def test_returns_dashboard(self):
        factory = RequestFactory()
        request = factory.get("/app/dashboard")
        result = app_section(request)
        assert "app_section" in result
        assert result["app_section"] == "dashboard"
