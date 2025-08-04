from django.urls import path, include
from cars import views
from reviews.views import CreateReviewAPIView, GetReviewAPIView

urlpatterns = [
    path('', views.CarCatalogView.as_view(), name='cars-dashboard'),
    path('add/', views.CreateCarView.as_view(), name='create-car'),
    path('<int:pk>/', include([
        path('details/', views.CarDetailsView.as_view(), name='car-details'),
        path('edit/', views.EditCarView.as_view(), name='edit-car'),
        path('delete/', views.DeleteCarView.as_view(), name='delete-car'),
        path('approve/', views.approve_car, name='approve-car'),
        path('deny/', views.deny_car, name='deny-car'),
        path('review/', CreateReviewAPIView.as_view(), name='create-review'),
        path('reviews/', GetReviewAPIView.as_view(), name='list-review')

    ]))
]
