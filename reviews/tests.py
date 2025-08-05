from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase
from cars.models import Car
from reviews.models import Review

UserModel = get_user_model()


class TestReviewModel(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(
            email='user@test.com',
            password='test1234',
        )

        self.car = Car.objects.create(
            owner=self.user,
            make='BMW',
            model_name='M3',
            horse_power=400,
            year='2024-01-01',
            price_per_hour=100,
            engine_size=3000,
            body_type='Sedan',
            fuel_type='Gas',
            image='cars/test.jpg',
            approved=True,
        )

    def test__str__returns_correct_string(self):
        review = Review.objects.create(
            car=self.car,
            reviewer=self.user,
            comment='Great car!',
            rating=5,
        )

        self.assertEqual(str(review), f'Reviewed by {self.user}')

    def test__rating_out_of_range__raises_validation_error(self):
        review = Review(
            car=self.car,
            reviewer=self.user,
            comment='Bad rating',
            rating=7,
        )

        with self.assertRaises(ValidationError) as ve:
            review.full_clean()

        self.assertEqual("The rating must be between 1 and 5", ve.exception.messages[0])
