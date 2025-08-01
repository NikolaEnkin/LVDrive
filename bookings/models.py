from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

from bookings.choices import BookingStatusChoices
from cars.models import Car


UserModel = get_user_model()

class Booking(models.Model):

    booker = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name='user_bookings'
    )

    car = models.ForeignKey(
        to=Car,
        on_delete=models.CASCADE,
        related_name='car_bookings',
    )

    start_datetime = models.DateTimeField()

    end_datetime = models.DateTimeField()

    status = models.CharField(
        max_length=20,
        choices=BookingStatusChoices,
        default=BookingStatusChoices.PENDING
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )


    def clean(self) -> str or None:
        if self.start_datetime and self.end_datetime:
            curr_time = timezone.now()
            if self.end_datetime <= self.start_datetime:
                raise ValidationError("End time must be after the start time!")
            if self.start_datetime <= curr_time:
                raise ValidationError("Start time must be in the future!")

            if not self.car_id:
                return



            overlap_booking = Booking.objects.filter(
                car=self.car,
                start_datetime__lt=self.end_datetime,
                end_datetime__gt=self.start_datetime,
                status='ACTIVE'
            ).exclude(pk=self.pk).exists()

            if overlap_booking:
                raise ValidationError("The car is already booked for this period")


    def save(self, *args, **kwargs) -> None:
        self.full_clean()

        if self._state.adding:
            self.status = BookingStatusChoices.ACTIVE
        super().save(*args, **kwargs)





