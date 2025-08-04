from rest_framework import serializers
from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    reviewer_email = serializers.CharField(source='reviewer.email', read_only=True)

    class Meta:
        model = Review
        fields = ['comment', 'created_at', 'rating', 'reviewer_email']
        read_only_fields = ['reviewer', 'car', 'created_at']