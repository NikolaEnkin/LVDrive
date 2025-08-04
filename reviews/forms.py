from django import forms

from reviews.models import Review


class CreateReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment', 'rating']
