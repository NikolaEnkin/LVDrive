from django.urls import path

from bookings import views

urlpatterns = [
    path('add/<int:car_pk>/', views.CreateBookingView.as_view(), name='create-booking')
]