from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import zoom

class FormZoom(forms.ModelForm):
    user = forms.CharField(max_length=50, widget=forms.Textarea())
    conferma = forms.CharField( max_length=10, widget=forms.Textarea())
    casa = forms.CharField(max_length=50, widget=forms.Textarea())

    class Meta:
        model = zoom
        fields = ["user", "conferma", "casa"]
