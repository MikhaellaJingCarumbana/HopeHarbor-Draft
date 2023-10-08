from django.contrib import admin
from .models import Beneficiary, Address

class AddressAdmin(admin.ModelAdmin):
    list_display = ('house_number', 'street', 'barangay', 'city', 'state')
    search_fields = ('house_number', 'street', 'barangay', 'city', 'state')

class BeneficiaryAdmin(admin.ModelAdmin):
    list_display = ('UserID', 'FirstName', 'LastName', 'EmailAddress', 'UserType', 'Needs')
    list_filter = ('UserType', 'Needs')
    search_fields = ('FirstName', 'LastName', 'EmailAddress')

# Register the models with their respective admin classes
admin.site.register(Address, AddressAdmin)
admin.site.register(Beneficiary, BeneficiaryAdmin)