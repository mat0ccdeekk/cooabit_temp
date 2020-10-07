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
def emailConImmagine(name_email, testo):
    name_email = {"luigiforziati@gmail.com": "Luigi", "farah.01.mohamed@gmail.com": "Mohamed", "benjamin20302@gmail.com": "Benjamin",
    "angechen98@gmail.com": "Angelica", "castagnastefano1998@gmail.com": "Stefano", "gui.balestrieri@gmail.com": "guido",
    "corrado340@gmail.com": "Corrado", "aci87@libero.it": "Andrea", "lorenzo.catale@libero.it": "Lorenzo", "ilenia.careddu@gmail.com": "Ilenia",
    "sergioguadltieri1992@gmail.com": "sergio", "simone.larocca@outlook.com": "Simone", "mattia.lavecchia@gmail.com": "Mattia",
    "sekenrico14@gmail.com": "Enrico", "benedetta.difrancoo@gmail.com": "Benedetta", "giuliavalentep@gmail.com": "Giulia",
    "pratiallegra@hotmail.it": "Allegra", "maria.falasco97@gmail.com": "Maria", "martaparisi.1995@gmail.com": "Marta", "samu.rubi@gmail.com": "Samuele",
    "francesco.pressi95@gmail.com": "Francesco", "massimanenti.mm@gmail.com": "Massimiliano", "i.ciccone@outlook.it": "iole",
    "martina.cairoli@ymail.com": "Martina", "zio.zizi21@gmail.com": "Lorenzo", "conversopaolo@gmail.com": "Paolo", "nica322000@gmail.com": "Veronica",
    "annaniedda@gmail.com": "Anna", "Gabriele.berio@gmail.com": "Gabriele"}

    sender_email = "cooabit@gmail.com"

    for key in name_email:
        receiver_email = key

        msg = MIMEMultipart()
        msg['Subject'] = 'Cerchi ancora una stanza a Milano ?'
        msg['From'] = sender_email
        msg['To'] = receiver_email
        testoNew = testo.replace('name', name_email[key])
        msgText = MIMEText(testoNew, 'html')
        msg.attach(msgText)
        # with open('/home/gigino/Scrivania/demoEnv1/social_site/accounts/cooabit.png', 'rb') as fp:
        #     img = MIMEImage(fp.read())
        #     img.add_header('Content-Disposition', 'attachment', filename="cooabit.png")
        #     msg.attach(img)
        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as smtpObj:
                smtpObj.ehlo()
                smtpObj.starttls()
                smtpObj.login("cooabit@gmail.com", "Ciao@1234")
                smtpObj.sendmail(sender_email, receiver_email, msg.as_string())
        except Exception as e:
            print(e)

def getEmailAndName():
    email_exclude = ['service.homehotel@gmail.com', 'mattia.raffaelli@the-roommate.com', 'mattialavecchia@gmail.com', "sergio.gualtieri@gmail.com",
    'ilovevintage.milano@gmail.com', 'maryecom@gmail.com', 'raffavis55@gmail.com', 'lughislandi@hotmail.com',
    'm.washington747@gmail.com', 'info-servizi@email.it', 'veronica.exogroove@gmail.com', 'sergiolucchetto@gmamil.com', "sergiogualtieri1@aol.com",
    'ciatinha@hotmail.com', 'service.homehotel@gmail.com', 'mattia.raffaelli@the-roommate.com', 'mattiaraffaelli22@gmail.com',
    'ciao@ciao.com', 'gigino@gigino.cz', 'sergiogualtieri@aol.com', 'eva@kant.it', 'pinolavecchia@gmail.com', 'patopato@gmail.com', 'sergioguadltieri1992@gmail.com']
    user = User.objects.all()
    userSub = subscription.objects.all()
    name_email = {}

    for u in user:
        if u.email not in email_exclude:
            name_email[u.email] = u.first_name
            # print(name_email[u.email])

    for s in userSub:
        if s.email not in email_exclude:
            name_email[s.email] = s.nome
    file1 = open("email_nome.txt","w")
    for nm in name_email:
        # print(nm," ",name_email[nm])
        stringa = nm+", "+name_email[nm]+"\n"
        file1 = open("email_nome.txt", "a")
        file1.write(stringa)
    file1.close()



    return name_email


def MandaEmail(request):
    name_email = getEmailAndName()
    if request.method == "POST":
        email_form = FormEmail(request.POST)
        print(email_form)
            # messages.add_message(request, messages.ERROR, 'Email già esistente')
        if email_form.is_valid() :
            testo = email_form.cleaned_data["email"]
            print("TESTO : ",testo)

            emailConImmagine(name_email, testo)
            messages.add_message(request, messages.SUCCESS, 'Email mandata con successo')
        else:
            print("form non valid")
    else:
        email_form = FormEmail()
        print("Creazione form email")

    emailLista = name_email.keys()
    context = {"email": emailLista, "form": email_form}
    return render(request, 'accounts/manda_email.html', context)


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
