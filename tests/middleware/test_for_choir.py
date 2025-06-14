from http import HTTPStatus

from django.core.cache import cache
from django.test import TestCase

from choirs.models import Choir


class TestCheckForChoirMiddleware(TestCase):
    def setUp(self):
        cache.clear()

    def test_redirects_to_initial_setup(self):
        response = self.client.get("/")
        self.assertRedirects(response, "/initial-setup")

    def test_does_not_redirect_with_existing_choir(self):
        Choir.objects.create(name="Fake Choir", description="Fake Choir Description")
        response = self.client.get("/")
        assert response.status_code == HTTPStatus.OK
