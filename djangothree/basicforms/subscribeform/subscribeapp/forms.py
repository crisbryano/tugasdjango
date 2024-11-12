from django import forms
from subscribeapp.models import Customer  # Assuming you have a Customer model

class NewSubs(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email']  # Example fields
