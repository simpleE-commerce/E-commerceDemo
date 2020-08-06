from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email_address = forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder': 'Email Address'}),
        label=''
    )
    password1 = forms.CharField(
        max_length=16,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter your password'}
        ),
        label=''
    )
    password2 = forms.CharField(
        max_length=16,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}
        ),
        label=''
    )

    class Meta:
        model = User
        fields = ['username', 'email_address', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Your Username'}),
        }
        labels = {
            'username': '',
        }
        help_texts = {
            'username': ''
        }
