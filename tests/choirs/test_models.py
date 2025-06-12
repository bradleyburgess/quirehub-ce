from typing import cast

import pytest
from django.contrib.auth import get_user_model
from faker import Faker

from choirs.models import Choir


class TestChoir:
    fake = Faker()

    @pytest.mark.django_db
    def test_choir_has_user(self):
        User = get_user_model()
        email = self.fake.email()
        password = self.fake.password()
        user = User.objects.create_user(email=email, password=password)  # type: ignore
        choir = Choir.objects.create(
            name="Fake Choir",
            description="Fake Choir Description",
            created_by=user,
        )
        assert choir.created_by == user

    def test_str(self):
        name = self.fake.name()
        choir = Choir(name=name, description="")
        assert str(choir) == name

    @pytest.mark.django_db
    def test_choir_has_null_user_after_user_deletion(self):
        User = get_user_model()
        email = self.fake.email()
        password = self.fake.password()
        user = User.objects.create_user(email=email, password=password)  # type: ignore
        choir = Choir.objects.create(
            name="Fake Choir",
            description="Fake Choir Description",
            created_by=user,
        )
        user.delete()
        choir = cast(Choir, Choir.objects.first())
        assert choir.created_by is None
