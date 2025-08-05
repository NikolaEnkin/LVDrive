from datetime import timedelta
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone
from django.core.exceptions import ValidationError
from bookings.models import Booking
from cars.models import Car

UserModel = get_user_model()

class TestBookingModel(TestCase):
    def setUp(self):

        self.user = UserModel.objects.create_user(
            email="email@test.com",
            password="test1234"
        )

        self.booker = UserModel.objects.create_user(
            email='booker@test.com',
            password='test1234'
        )

        self.car = Car.objects.create(
            owner=self.user,
            make='BMW',
            model_name='M4',
            horse_power=500,
            year='2024-01-01',
            price_per_hour=50,
            engine_size=3000,
            body_type='Sedan',
            fuel_type='Gas',
            image='cars/test.jpg',
            approved=True,
        )

    def test__create_valid_booking(self):
        start_time = timezone.now() + timedelta(days=1)
        end_time = timezone.now() + timedelta(days=3)

        booking = Booking.objects.create(
            booker=self.booker,
            car=self.car,
            start_datetime=start_time,
            end_datetime=end_time,
        )

        self.assertEqual(booking.booker, self.booker)
        self.assertEqual(booking.car, self.car)
        self.assertEqual(booking.status, 'ACTIVE')

    def test__booking_invalid_dates__raise_error(self):
        start_time = timezone.now() + timedelta(days=1)
        end_time = timezone.now() + timedelta(days=-2)


        with self.assertRaises(ValidationError) as ve:
            booking = Booking(
                booker=self.booker,
                car=self.car,
                start_datetime=start_time,
                end_datetime=end_time,
            )
            booking.full_clean()

        self.assertEqual(
            ve.exception.messages[0],
            'End time must be after the start time!'
        )

        start_time = timezone.now() + timedelta(days=-1)
        end_time = timezone.now() + timedelta(days=2)

        with self.assertRaises(ValidationError) as ve:
            booking = Booking(
                booker=self.booker,
                car=self.car,
                start_datetime=start_time,
                end_datetime=end_time,
            )
            booking.full_clean()

        self.assertEqual(
            ve.exception.messages[0],
            'Start time must be in the future!'
        )

    def test__booing_overlapping_date__raises_error(self):
        start_time = timezone.now() + timedelta(days=1)
        end_time = timezone.now() + timedelta(days=3)

        booking = Booking.objects.create(
            booker=self.booker,
            car=self.car,
            start_datetime=start_time,
            end_datetime=end_time,
        )

        with self.assertRaises(ValidationError) as ve:
            booking2 = Booking.objects.create(
                booker=self.booker,
                car=self.car,
                start_datetime=start_time,
                end_datetime=end_time,
            )

        self.assertEqual(
            ve.exception.messages[0],
            'The car is already booked for this period'
        )
