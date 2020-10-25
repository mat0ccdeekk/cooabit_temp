from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import FormRegistrazione, ProfileForm, ProfileFormP, FormEmail

from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from .utils import generate_token
from django.core.mail import EmailMessage
from django.conf import settings
from django.views import View
from .models import Profile
from core.models import subscription

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication

# Create your views here.
def signup(request):
    return render(request, 'signup.html')
    
def PrivacyView(request):
    return render(request, 'accounts/privacy.html')

def ConditionView(request):
    return render(request, 'accounts/condizioni.html')

def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.profile.bio = 'ciao '
    user.save()

def registrazione(user_form, profile_form, request):
    first_name = user_form.cleaned_data["first_name"]
    last_name = user_form.cleaned_data["last_name"]
    email = user_form.cleaned_data["email"]
    password = user_form.cleaned_data["password1"]
    profile = profile_form.save(commit=False)
    User.objects.create_user(username=email, first_name=first_name, last_name=last_name, email=email, password=password)
    user = authenticate(username=email, password=password)
    profile.user = user
    user.is_active = False
    profile.save()

    current_site=get_current_site(request)
    email_subject='Attiva il tuo account cooabit',
    message=render_to_string('accounts/activate.html',
    {
        'user':user,
        'domain':current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': generate_token.make_token(user)
    })

    email_message = EmailMessage(
        email_subject,
        message,
        settings.EMAIL_HOST_USER,
        [email]
    )
    email_message.send()

class ActivateAccountView(View):
    def get(self, request, uidb64, token):
        try:
            uid=force_text(urlsafe_base64_decode(uidb64))
            user=User.objects.get(pk=uid)
        except Exception as identifier:
            user=None

        if user is not None and generate_token.check_token(user, token):
            user.is_active=True
            user.save()
            messages.add_message(request, messages.SUCCESS, 'Account attivato con successo')
            return redirect('login')
        return render(request, 'accounts/activate_fallita.html', status=401)

def RegistrazioneView(request):
    if request.method == "POST":
        user_form = FormRegistrazione(request.POST)
        profile_form = ProfileForm(request.POST)
        if User.objects.filter(email=request.POST.get('email')).exists():
            messages.add_message(request, messages.ERROR, 'Email già esistente')
            return render(request, 'accounts/registrazione.html', {"form": user_form, "formProfile": profile_form})
        if user_form.is_valid() and profile_form.is_valid():
            registrazione(user_form, profile_form, request)
            messages.add_message(request, messages.SUCCESS, 'Bene, ora verifica il tuo account, clicca sul link che ti abbiamo inviato per email')
            return redirect('login')
    else:
        user_form = FormRegistrazione()
        profile_form = ProfileForm()
    context = {"form": user_form, "formProfile": profile_form}
    return render(request, 'accounts/registrazione.html', context)


def RegistrazioneViewP(request):
    if request.method == "POST":
        user_form = FormRegistrazione(request.POST)
        profile_form = ProfileFormP(request.POST)
        if User.objects.filter(email=request.POST.get('email')).exists():
            messages.add_message(request, messages.ERROR, 'Email già esistente')
            return render(request, 'accounts/registrazioneP.html', {"form": user_form, "formProfileP": profile_form})
        if user_form.is_valid() and profile_form.is_valid():
            registrazione(user_form, profile_form, request)
            messages.add_message(request, messages.SUCCESS, 'Bene, ora verifica il tuo account, clicca sul link che ti abbiamo inviato per email')
            return redirect('login')
    else:
        user_form = FormRegistrazione()
        profile_form = ProfileFormP()
    context = {"form": user_form, "formProfileP": profile_form}
    return render(request, 'accounts/registrazioneP.html', context)
