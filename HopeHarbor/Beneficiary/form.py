from django import forms
from .models import Beneficiary, Address

class AddressForm(forms.ModelForm):
    house_number = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'House Number'})
    )
    street = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Street'})
    )
    barangay = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Barangay'})
    )
    city = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'City'})
    )
    state = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'State'})
    )

    class Meta:
        model = Address
        fields = ['house_number', 'street', 'barangay', 'city', 'state']

class BeneficiaryForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )
    firstname = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'First Name'})
    )
    middlename = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Middle Name'})
    )
    lastname = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'})
    )

    class Meta:
        model = Beneficiary
        fields = ['username', 'password', 'firstname', 'middlename', 'lastname', 'Needs', 'Address']
