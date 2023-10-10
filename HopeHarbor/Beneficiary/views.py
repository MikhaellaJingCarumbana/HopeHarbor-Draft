from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .form import BeneficiaryForm, AddressForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

# Create your views here.


def index(request):
    return  HttpResponse("hello world");


class BeneficiaryRegistration(View):
    template_name = 'create_beneficiary.html'  # Replace with your template file

    def get(self, request):
        beneficiary_form = BeneficiaryForm()  # Create an instance of BeneficiaryForm
        address_form = AddressForm()  # Create an instance of AddressForm
        return render(request, self.template_name, {'beneficiary_form': beneficiary_form, 'address_form': address_form})

class BeneficiaryLoginView(LoginView):
    template_name = 'login_donor.html'  # Specify the path to your login template
    success_url = reverse_lazy('beneficiary:index')  # Redirect to a success page after login
