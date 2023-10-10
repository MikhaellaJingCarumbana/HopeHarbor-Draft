from django.urls import path
from . import views


app_name = 'Donor'
urlpatterns = [
    path('', views.index, name='index'), #127.0.0.1/account
    path('register/', views.DonorRegistration.as_view(), name='registration'),
]
