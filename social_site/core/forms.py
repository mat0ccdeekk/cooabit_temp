from django import forms
from .models import subscription

class SubscriptionForm(forms.ModelForm):

    class Meta:
        model = subscription
        fields = ['nome', 'cognome' , 'email']
