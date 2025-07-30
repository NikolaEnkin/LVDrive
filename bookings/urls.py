from django.urls import path, include
from bookings import views

urlpatterns = [
    path('<int:pk>/', include([
        path('add/', views.CreateBookingView.as_view(), name='create-booking'),
        path('edit/', views.EditBookingView.as_view(), name='edit-booking'),
    ])),
]