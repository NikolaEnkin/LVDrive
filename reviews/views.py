from django.shortcuts import render, get_object_or_404
from rest_framework import generics, permissions
from cars.models import Car
from reviews.models import Review
from reviews.serializers import ReviewSerializer


class CreateReviewAPIView(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        car = get_object_or_404(Car, pk=self.kwargs.get('pk'))

        serializer.save(
            car=car,
            reviewer=self.request.user
        )


class GetReviewAPIView(generics.ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        car = get_object_or_404(Car, pk=self.kwargs.get('pk'))
        return Review.objects.filter(car=car).select_related('reviewer')
