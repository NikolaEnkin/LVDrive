from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from accounts.models import Profile

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

class EditProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        exclude = ['user']

        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Enter your first name'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Enter your last name'
            }),
            'phone_number': forms.TextInput(attrs={
                'placeholder': 'Enter your phone number '
            }),
            'date_of_birth': forms.DateInput(attrs={
                'type': 'date'
            }),
            'driver_license_number': forms.DateInput(attrs={
                'type': 'date'
            }),
            'driver_license_expiry': forms.DateInput(attrs={
                'type': 'date'
            }),
        }


