from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django_resized import ResizedImageField
from PIL import Image
from accounts.models import ProfileP

# Create your models here.


class Casa(models.Model):
    """
    La piattaforma è divisa in base alla zona scelta
    per cercare la casa. Ciascuna casa contiene oltre
    ai propri dati, una interazione (thunder) da parte
    di un utente salvandola nel proprio profilo.

    blank = True ---> campo richiesto
    null = True ---> relativo al db, la colonna acetta valori null
    """
    #nome_agenzia = models.CharField(max_length=30)
    #nome_proprietario = models.CharField(max_length=30)
    #area = models.CharField(max_length=30)
    active = models.CharField(blank=True, null=True, default="False", max_length=10)
    mesiCaparra = models.IntegerField(blank=True, null=True, default="0")


    citta = models.CharField(max_length=40)
    zona = models.CharField(blank=True, null=True, max_length=40, default="none")
    via = models.CharField(blank=True, null=True, max_length=40, default="none")

    tipo_immobile = models.CharField(blank=True, null=True, max_length=100, default="none")
    piano = models.CharField(blank=True, null=True, max_length=40, default="none")

    m_quadri = models.IntegerField(blank=True, null=True)

    studenti = models.CharField(blank=True, null=True, default="none", max_length=10)
    animali = models.CharField(blank=True, null=True, max_length=40, default='none')
    ascensore = models.CharField(blank=True, null=True, max_length=40, default='none')
    ariaCond = models.CharField(blank=True, null=True, max_length=40, default="none")
    wifi = models.CharField(blank=True, null=True, max_length=40, default="none")
    tv = models.CharField(blank=True, null=True, max_length=40, default="si")
    riscaldamento = models.CharField(blank=True, null=True, max_length=40, default="si")
    lavatrice = models.CharField(blank=True, null=True, max_length=40, default="si")

    stanzaDoppia = models.IntegerField(blank=True, null=True, default="0")
    stanzaSingola = models.IntegerField(blank=True, null=True, default="0")
    stanzaTripla = models.IntegerField(blank=True, null=True, default="0")
    postiTotali = models.IntegerField(blank=True, null=True)
    bagni = models.IntegerField(blank=True, null=True, default='0')
    balconi = models.IntegerField(blank=True, null=True, default='0')
    coinquiliniPresenti = models.IntegerField(blank=True, null=True, default='0')

    prezzo = models.IntegerField()
    prezzoCondominio = models.IntegerField(blank=True, null=True)

    descrizione = models.TextField(blank=True, null=True)
    thunders = models.ManyToManyField(User, related_name='thunders', blank=True)
    owner = models.ForeignKey(ProfileP, related_name='owners', on_delete=models.CASCADE, default="")

    foto1 = models.ImageField(blank=True, null=True, default="none")
    foto2 = models.ImageField(blank=True, null=True, default="none")
    foto3 = models.ImageField(blank=True, null=True, default="none")
    foto4 = models.ImageField(blank=True, null=True, default="none")
    foto5 = models.ImageField(blank=True, null=True, default="none")
    foto6 = models.ImageField(blank=True, null=True, default="none")
    foto7 = models.ImageField(blank=True, null=True, default="none")
    foto8 = models.ImageField(blank=True, null=True, default="none")
    foto9 = models.ImageField(blank=True, null=True, default="none")
    foto10 = models.ImageField(blank=True, null=True, default="none")
    foto11 = models.ImageField(blank=True, null=True, default="none")
    foto12 = models.ImageField(blank=True, null=True, default="none")
    foto13 = models.ImageField(blank=True, null=True, default="none")
    foto14 = models.ImageField(blank=True, null=True, default="none")
    foto15 = models.ImageField(blank=True, null=True, default="none")
    foto16 = models.ImageField(blank=True, null=True, default="none")

    # image = models.FileField(null=True, blank=True, default="none")


    def __str__(self):
        return self.citta+str(self.id)

    def get_absolute_url(self):
        return reverse("visualizza_casa", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "Casa"
        verbose_name_plural = "Case"



class Recensione(models.Model):
    """
    Un utente potrà lasciare una recensione per la casa/stanza dove ha vissuto
    """
    contenuto = models.TextField()
    data_creazione = models.DateTimeField(auto_now_add = True)
    utente_recensione = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recensioni")
    casa_recensione = models.ForeignKey(Casa, on_delete=models.CASCADE)

    def __str__(self):
        return self.utente_recensione.username+" - "+self.casa_recensione.nome

    class Meta:
        verbose_name = "Recensione"
        verbose_name_plural = "Recensioni"
