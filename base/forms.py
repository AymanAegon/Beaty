from django.contrib.auth.forms import UserCreationForm
from .models import User, Beat
from django.forms import ModelForm
from django import forms


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

        widgets = {
            'first_name': forms.TextInput(attrs={'id': 'fname', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'id': 'lname', 'placeholder': 'Last Name'}),
            'username': forms.TextInput(attrs={'id': 'username', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'id': 'email', 'placeholder': 'Email'}),
            'password1': forms.PasswordInput(attrs={'id': 'password1', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'id': 'password2', 'placeholder': 'Repeat your password'}),
        }
        
class BeatForm(ModelForm):
    class Meta:
        model = Beat
        fields = ['name']

class EditUser(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'bio', 'profile_img']