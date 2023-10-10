# views.py
from django.shortcuts import render, get_object_or_404
from .models import Donor
from django.http import HttpResponse
from django.views import View
from .form import DonorForm


def home(request):
    return render(request, 'home.html', {})


def index(request):
    return HttpResponse("hello world")


class DonorRegistration(View):
    template = 'registration.html'

    def get(self, request):
        donor = DonorForm()
        return render(request, self.template, {'form': donor})




