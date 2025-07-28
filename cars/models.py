from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone

from cars.choices import CarBodyTypeChoices, CarFuelTypeChoices
from cars.validators import CarEngineSizeValidator


UserModel = get_user_model()

class Car(models.Model):

    owner = models.ForeignKey(
        to=UserModel,
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
        default=CarBodyTypeChoices.SEDAN
    )

    fuel_type = models.CharField(
        max_length=10,
        choices=CarFuelTypeChoices,
        default=CarFuelTypeChoices.OTHER,
    )


    image = models.ImageField(
        upload_to='cars/',
    )

    @property
    def is_available(self):
        return self.car_bookings.filter(status='ACTIVE').exists()

    @property
    def get_owner(self):
        curr_time = timezone.now()
        booking = self.car_bookings.filter(
            start_datetime__lte=curr_time,
            end_datetime__gte=curr_time,
            status='ACTIVE'
        ).select_related('owner__profile').first()

        return booking.owner_id if booking else None


class CarImage(models.Model):
    car = models.ForeignKey(
        to=Car,
        on_delete=models.CASCADE,
        related_name='car_images'
    )

    car_image = models.ImageField(
        upload_to='car_extra_photos/'
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )







