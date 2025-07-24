from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models
from cars.choices import CarBodyTypeChoices, CarFuelTypeChoices
from cars.validators import CarEngineSizeValidator


class Car(models.Model):

    owner = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='cars',
    )

    make = models.CharField(
        max_length=50,
    )

    model_name = models.CharField(
        max_length=50,
    )

    horse_power = models.PositiveIntegerField()

    year = models.DateField()

    price_per_hour = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        validators=[
            MinValueValidator(0, message='The price cannot be negative')
        ]
    )

    engine_size = models.IntegerField(
        validators=[
            CarEngineSizeValidator(),
        ]
    )

    body_type = models.CharField(
        max_length=30,
        choices=CarBodyTypeChoices,
    )

    fuel_type = models.CharField(
        max_length=10,
        choices=CarFuelTypeChoices,
        default=CarFuelTypeChoices.OTHER,
    )


    image = models.ImageField(
        upload_to='cars/',
    )







