
from django import forms
from .models import Customers,DistributionRequired

class AddCustomer(forms.ModelForm):
    class Meta:
        model = Customers
        fields = ['user_id','name', 'mobile', 'address', 'pincode', 'type_of_customer','is_active','is_archived']

class UpdateCustomer(forms.ModelForm):
    class Meta:
        model = Customers
        fields = ['name', 'mobile', 'address', 'pincode', 'type_of_customer']

class MilkDistribution(forms.ModelForm):
    class Meta:
        model = DistributionRequired
        fields = ['type_of_milk','price','unit','time_of_delivery']

'''
class AddCustomer(forms.Form):
    user_id= forms.CharField(max_length=32)
    name = forms.CharField(max_length=100)
    mobile = forms.CharField(max_length=10)
    address = forms.CharField(max_length=300)
    pincode = forms.CharField(max_length=6)
    
    customer_type =(('individual','individual'),('professional','professional'),)
    type_of_customer = forms.ChoiceField( choices=customer_type)

    is_archived = forms.BooleanField()

'''
