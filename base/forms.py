from django.contrib.auth.forms import UserCreationForm
from .models import User, Beat
from django.forms import ModelForm


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class BeatForm(ModelForm):
    class Meta:
        model = Beat
        fields = ['name']