from django.urls import path

from home import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about-us', views.AboutUsView.as_view(), name='about-us')
]