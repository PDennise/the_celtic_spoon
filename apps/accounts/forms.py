from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ARegistrationForm(UserCreationForm):      # Inheriting from UserCreationForm
    class Meta:                                 # Defines additional configurations for the form
        model = User                            # Specify the model associated with this form
        fields = ['username', 'email', 'password1', 'password2'] # Define the fields to include in the form