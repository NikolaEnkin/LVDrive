from django.contrib.auth import get_user_model
from django.db import models
from cars.models import Car
from reviews.validators import ReviewRatingValidator

UserModel = get_user_model()

class Review(models.Model):

    car = models.ForeignKey(
        to=Car,
        on_delete=models.CASCADE,
        related_name='car_reviews'
    )

    reviewer = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name='user_reviews'
    )

    comment = models.TextField()

    rating = models.PositiveIntegerField(
        validators=[
            ReviewRatingValidator(),
        ]
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )


    class Meta:
        unique_together = ['car', 'reviewer']

    def __str__(self):
        return f'Reviewed by {self.reviewer}'





