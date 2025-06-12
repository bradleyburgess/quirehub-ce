from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


class AdminSignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update({"autofocus": False})
        self.fields["password1"].help_text = (
            "Your password should be 12 characters or more, and contain upercase"
            "and lowercase letters, numbers, and symbols"
        )

    class Meta:
        model = User
        fields = (
            "email",
            "first_name",
            "last_name",
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        if commit:
            user.save()
        return user
