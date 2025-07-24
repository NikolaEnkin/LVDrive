from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MinLengthValidator
from django.db import models
from accounts.managers import AppUserManager
from accounts.validators import ProfileNameValidator, PhoneNumberValidator


class AppUser(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'email'

    email = models.EmailField(
        unique=True,
        error_messages={
            'unique': "User with this email already exists!"
        }
    )

    is_active = models.BooleanField(
        default=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    objects = AppUserManager()

    def __str__(self) -> str:
        return self.email

class Profile(models.Model):
    user = models.OneToOneField(
        to=AppUser,
        on_delete=models.CASCADE,
        related_name='profile',
    )

    first_name = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        validators=[
            MinLengthValidator(2, message="First name needs to be at least 2 characters long!"),
            ProfileNameValidator(),
        ]
    )

    last_name = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        validators=[
            MinLengthValidator(2, "Last name needs to be at least 2 characters long!"),
            ProfileNameValidator(),
        ],
    )

    phone_number = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        validators=[
            MinLengthValidator(10, message='The phone number must be exactly 10 digits long!'),
            PhoneNumberValidator(),
        ],
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    driver_license_number = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    driver_license_expiry = models.DateField(
        null=True,
        blank=True,
    )

    profile_image = models.ImageField(
        upload_to = 'profiles/',
        blank = True,
        null = True
    )
    
    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        elif self.first_name and not self.last_name:
            return self.first_name
        elif not self.first_name and self.last_name:
            return self.last_name

        return self.user.email






