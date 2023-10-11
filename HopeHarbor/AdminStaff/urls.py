from django.urls import path
from . import views

app_name = 'AdminStaff'

urlpatterns = [
    path('', views.index, name='index'), #127.0.0.1/account
    path('reg/', views.AdminStaffRegistration.as_view(), name='reg'),
    path('login/', views.AdminStaffLogin.as_view(), name='login')
]