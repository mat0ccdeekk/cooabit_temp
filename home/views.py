from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, HttpResponse, redirect
from django.views.generic.edit import CreateView
from .forms import CasaForm
from .mixins import StaffMixing
from .models import Casa
import time
import os


def CreaCasa(request, pk):
    print("siamo ancora qua")
    if request.method == "POST":
        form_casa = CasaForm(request.POST, request.FILES)
        print(form_casa)
        if form_casa.is_valid():
            folder = ""
            tempo = ""
            # folder += tempo
            # print("tempo ",tempo)
            # print("nome cartella", folder)
            # folder = request.user.first_name+"_"+request.user.last_name
            # tempo = time.ctime()
            # settings.MEDIA_ROOT=os.path.join(os.path.dirname(BASE_DIR), 'media-serve/'+folder)
            form_casa.save()
            return HttpResponseRedirect("/")
        else:
            print("form_casa not valid")

    print("view")
    form_casa = CasaForm()
    context = {"casa": form_casa}
    return render(request, "home/crea_casa.html", context)


"""
def CreaCasa(request, pk):
    print("siamo ancora qua")
    if request.method == "POST":
        print("vediamoooo",request.FILES)
        form_gallery = GalleryForm(request.POST, request.FILES)
        form_casa = CasaForm(request.POST)
        print(form_gallery)
        print(form_casa)
        if form_casa.is_valid():
            if form_gallery.is_valid():

                newGallery = form_gallery.save(commit=False)
                form_casa.gallery = newGallery
                form_casa.save()
                return HttpResponseRedirect("/")
            else:
                print("form_gallery not valid")
        else:
            print("form_casa not valid")

    print("view")
    form_gallery = GalleryForm()
    form_casa = CasaForm()
    context = {"casa": form_casa, "form_gallery": form_gallery}
    return render(request, "home/crea_casa.html", context)
"""

def visualizzaCasa(request, pk):
    casa = get_object_or_404(Casa, pk=pk)
    if casa.prezzo > 0 and casa.postiTotali > 0:
        prezzoStudente = casa.prezzo / casa.postiTotali
    via = ""
    if casa.zona != "none":
        via = via + casa.zona
    if casa.via != "none":
        via = casa.via
    context = {"casa": casa, "prezzoStudente": prezzoStudente, "via": via}
    return render(request, "detail-rooms.html", context)

def creaThunder(request, pk):
    casa = get_object_or_404(Casa, pk=pk)

#ciao talebano come stai??
## TODO: sto bene
