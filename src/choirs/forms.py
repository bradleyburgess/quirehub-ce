from django.forms import ModelForm

from .models import Choir


class ChoirCreateForm(ModelForm):
    class Meta:
        model = Choir
        fields = ["name", "description"]
