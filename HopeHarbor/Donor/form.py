from django.forms import ModelForm
from django import forms
from .models import Donor


class DonorForm(ModelForm):
    FirstName = forms.CharField(widget=forms.TextInput)
    LastName = forms.CharField(widget=forms.TextInput)
    Username = forms.CharField(widget=forms.TextInput)
    EmailAddress = forms.CharField(widget=forms.TextInput)
    Password = forms.CharField(widget=forms.PasswordInput)
    DonationType = forms.CharField(widget=forms.HiddenInput, initial="")
    UserType = forms.CharField(widget=forms.HiddenInput, initial="donor")

    class Meta:
        model=Donor
        fields = ['FirstName', 'LastName', 'Username', 'EmailAddress', 'Password', 'DonationType', 'UserType']
