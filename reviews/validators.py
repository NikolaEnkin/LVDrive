from typing import Optional
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class ReviewRatingValidator:
    def __init__(self, message: Optional[str]=None) -> None:
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value: Optional[str]) -> None:
        self.__message = value or "The rating must be between 1 and 5"

    def __call__(self, value: str) -> str:
        if not (1 <= value <= 5):
            raise ValidationError(self.message)

