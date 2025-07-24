from typing import Optional

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class ProfileNameValidator:
    def __init__(self, message: Optional[str]=None) -> None:
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value: Optional[str]) -> None:
        self.__message = value or "Check if both names are made of only letters"

    def __call__(self, value: str) -> str:
        if not value.isalpha():
            raise ValidationError(self.message)


@deconstructible
class PhoneNumberValidator:
    def __init__(self, message: Optional[str]=None) -> None:
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value: Optional[str]) -> None:
        self.__message = value or "The phone numbers must contain only digits"

    def __call__(self, value: str) -> str:
        if not value.isdigit():
            raise ValidationError(self.message)
