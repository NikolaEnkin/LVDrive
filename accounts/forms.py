from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

UserModel = get_user_model()

class AppUserCreationForm(UserCreationForm):

    class Meta:
        model = UserModel
        fields = ['email', 'password1', 'password2']


        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter your email'
            }),

            'password1': forms.PasswordInput(attrs={
                'label': 'Hello'
            })
        }

