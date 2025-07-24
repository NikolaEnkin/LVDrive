from typing import Optional
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class CarEngineSizeValidator:
    def __init__(self, message: Optional[str]=None) -> None:
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value: Optional[str]) -> None:
        self.__message = value or "The engine size cannot be smaller than 900cc and bigger than 5500cc"

    def __call__(self, value: str) -> str:
        if not (900 <= value <= 5500):
            raise ValidationError(self.message)

