from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, ProfileP
from social_site import settings

class FormEmail(forms.Form):
    email = forms.CharField(widget=forms.Textarea(attrs={'placeholder': "Esempio : <div calss='container'> <img src='https://www.cooabit.com/static/cooabit.png' height='0' width='160'> <br> Ciao <h2>name</h2>,come stai? </div> " }))

class FormRegistrazione(UserCreationForm):
    first_name = forms.CharField(label="", max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder': 'Nome' }))
    last_name = forms.CharField(label="", max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder': 'Cognome'}))
    email = forms.CharField(label="", max_length=50, required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(label="", max_length=50, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'password'}))
    password2 = forms.CharField(label="", max_length=50, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'verifica password'}))

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password1", "password2"]

class UpdateFormRegistrazione(forms.ModelForm):
    email = forms.EmailInput()

    class Meta:
        model = User
        fields = ["email"]

class ProfileForm(forms.ModelForm):
    sesso = (
        ('M', 'maschio'),
        ('F', 'femmina')
    )
    city = forms.CharField(label="", max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder': 'Città'}))
    occupation = forms.CharField(label="", max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder': 'Occupazione'}))
    age = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}, format=settings.DATE_INPUT_FORMATS), label="", required=False)
    gender = forms.ChoiceField(widget=forms.RadioSelect(), choices=sesso, label="", required=False)
    idZoom1 = forms.CharField(label="", max_length=300, widget=forms.Textarea(), required=False)
    idZoom2 = forms.CharField(label="", max_length=300, widget=forms.Textarea(), required=False)
    pass1 = forms.CharField(label="", max_length=300, widget=forms.Textarea(), required=False)
    pass2 = forms.CharField(label="", max_length=300, widget=forms.Textarea(), required=False)
    link1 = forms.CharField(label="", max_length=300, widget=forms.Textarea(), required=False)
    link2 = forms.CharField(label="", max_length=300, widget=forms.Textarea(), required=False)


    class Meta:
        model = Profile
        fields = ['city', 'occupation' , 'age', "gender", "state", "mobile", "photo", "aboutMe", "maxima", "pet", "idZoom1", "idZoom2", "pass1", "pass2", "link1", "link2"]


class ProfileFormP(forms.ModelForm):

    class Meta:
        model = ProfileP
        fields = ["mobile", "agency"]
