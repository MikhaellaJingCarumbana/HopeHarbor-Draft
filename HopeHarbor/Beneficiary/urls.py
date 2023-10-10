from django.urls import path
from . import views

app_name = 'Beneficiary'  # App namespace (optional but recommended)

urlpatterns = [
    path('', views.index, name='index'),  # 127.0.0.1/account
    path('reg', views.BeneficiaryRegistration.as_view(), name='reg'),
    path('log', views.BeneficiaryLoginView.as_view(), name='log')# Add more URL patterns as needed
]
