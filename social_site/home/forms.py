from django import forms
from .models import Casa

# class FileFieldForm(forms.ModelForm):
#
#     # file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
#     class Meta:
#         model = Photo
#         fields = ['file',]

class CasaForm(forms.ModelForm):
    Flag = (
        ('S', 'si'),
        ('N', 'no')
    )

    citta = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'città'}), max_length=40, label="", required=True)
    zona = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'zona'}), max_length=50, label="", required=True)
    via = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'via'}), max_length=40, label="", required=True)
    tipo_immobile = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'monolocale, bilocale, altro'}), max_length=80, label="", required=True)
    piano = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'specifica il piano'}), max_length=40, label="", required=False)

    m_quadri = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'metri quadri'}), label="", required=True)
    prezzo = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'prezzo'}), label="", required=True)
    stanzaSingola = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'n° singole'}), label="", required=False)
    stanzaDoppia = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'n° doppie'}), label="", required=False)
    stanzaTripla = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'n° triple'}), label="", required=False)
    prezzoCondominio = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'prezzo condominio'}), label="", required=False)
    postiTotali = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'posti totali'}), label="", required=False)

    bagni = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'n° bagni'}), label="", required=False)
    balconi = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'n° balconi'}), label="", required=False)
    coinquiliniPresenti = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'n° inquilini presenti'}), label="", required=False)
    mesiCaparra = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'n° mesi cappara'}), label="", required=False)

    studenti = forms.BooleanField(label="studenti", required=False)
    ascensore = forms.BooleanField(label="ascensore", required=False)
    ariaCond = forms.BooleanField(label="ariaCond", required=False)
    animali = forms.BooleanField(label="animali", required=False)
    wifi = forms.BooleanField(label="wifi", required=False)

    foto1 = forms.ImageField(required=False)
    foto2 = forms.ImageField(required=False)
    foto3 = forms.ImageField(required=False)
    foto4 = forms.ImageField(required=False)
    foto5 = forms.ImageField(required=False)
    foto6 = forms.ImageField(required=False)
    foto7 = forms.ImageField(required=False)
    foto8 = forms.ImageField(required=False)
    foto9 = forms.ImageField(required=False)
    foto10 = forms.ImageField(required=False)
    foto11 = forms.ImageField(required=False)
    foto12 = forms.ImageField(required=False)
    foto13 = forms.ImageField(required=False)
    foto14 = forms.ImageField(required=False)
    foto15 = forms.ImageField(required=False)
    foto16 = forms.ImageField(required=False)

    descrizione = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Altre info'}), label="", required=False)


    class Meta:
        model = Casa
        fields = ['citta', 'zona' , 'via', "piano", "ascensore", "m_quadri", "ariaCond",
        "postiTotali", "bagni","balconi", "stanzaSingola", "stanzaDoppia", "stanzaTripla",
        "coinquiliniPresenti", "prezzo", "wifi", "prezzoCondominio", "animali",
        "descrizione", "owner", "tipo_immobile", "mesiCaparra", "studenti",
        "foto1", "foto2", "foto3", "foto4", "foto5", "foto6", "foto7", "foto8",
        "foto9", "foto10", "foto11", "foto12", "foto13", "foto14", "foto15", "foto16"]
