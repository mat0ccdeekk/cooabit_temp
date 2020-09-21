from django.contrib import admin
from .models import Casa, Recensione
# Register your models here.

#aggiungiamo cose nella sezione admin


class CasaModelAdmin(admin.ModelAdmin):
    model = Casa
    list_display = ['citta', 'zona' , 'via', "piano", "ascensore", "m_quadri", "ariaCond",
    "postiTotali", "bagni","balconi", "stanzaSingola", "stanzaDoppia", "stanzaTripla",
    "coinquiliniPresenti", "prezzo", "wifi", "prezzoCondominio", "animali",
    "owner", "tipo_immobile", "mesiCaparra", "studenti", "active"]
    search_fields = ["citta","via","prezzo", "thunders"]
    list_filter = ["citta","via", "m_quadri","prezzo","thunders"]

class RecensioneModelAdmin(admin.ModelAdmin):
    model = Recensione
    list_display = ["utente_recensione","casa_recensione","data_creazione"]
    search_fields = ["contenuto"]
    list_filter = ["utente_recensione","casa_recensione","data_creazione"]



admin.site.register(Casa, CasaModelAdmin)
admin.site.register(Recensione, RecensioneModelAdmin)
