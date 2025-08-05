from datetime import timedelta

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils import timezone
from bookings.models import Booking
from cars.models import Car


UserModel = get_user_model()

class TestCarModel(TestCase):

    def setUp(self):
        self.user = UserModel.objects.create_user(
            email="email@test.com",
            password="test1234"
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

    def test__car_negative_price__raises_error(self):

        with self.assertRaises(ValidationError) as ve:
            self.car = Car(
                owner=self.user,
                make='BMW',
                model_name='M4',
                horse_power=500,
                year='2024-01-01',
                price_per_hour=-1000,
                engine_size=3000,
                body_type='Sedan',
                fuel_type='Gas',
                image='cars/test.jpg',
                approved=True,
            )

            self.car.full_clean()

        self.assertEqual(
            ve.exception.messages[0],
            'The price cannot be negative'
        )

    def test__is_available_property__true_if_active_booking_exists(self):
        booking = Booking.objects.create(
            car=self.car,
            booker=self.user,
            start_datetime=timezone.now() + timedelta(days=1),
            end_datetime=timezone.now() + timedelta(days=2),
            status='ACTIVE'
        )

        self.assertTrue(self.car.is_available)