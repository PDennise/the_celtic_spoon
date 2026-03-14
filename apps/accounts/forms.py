from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ARegistrationForm(UserCreationForm):
    """User registration form based on Django's UserCreationForm."""

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
