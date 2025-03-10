from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

# Form for user registration
class UserRegisterForm(UserCreationForm):
    location = forms.CharField(max_length=100, required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'location', 'password1', 'password2']