from django.urls import path, include
from cars import views

urlpatterns = [
    path('', views.CarCatalogView.as_view(), name='cars-dashboard'),
    path('add/', views.CreateCarView.as_view(), name='create-car'),
    path('<int:pk>/', include([
    path('details/', views.CarDetailsView.as_view(), name='car-details'),
    path('edit/', views.EditCarView.as_view(), name='edit-car'),
    path('delete/', views.DeleteCarView.as_view(), name='delete-car')
    ]))

]

