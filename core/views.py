from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from home.models import Casa
from django.http import HttpResponseRedirect
from accounts.forms import ProfileFormP, ProfileForm, UpdateFormRegistrazione
from .forms import SubscriptionForm
# Create your views here.

#def homepage(request):
#    return render(request, 'core/homepage.html')

def underCostructionPView(request):
    return render(request, 'core/underCostructionprop.html')

def about(request):
    return render(request, 'core/about.html')

def underCostructionView(request):
    if request.method == "POST":
        sub_form = SubscriptionForm(request.POST)
        if sub_form.is_valid():
            sub_form.save()
            return HttpResponseRedirect('/')

    sub_form = SubscriptionForm()
    context = {"sub_form": sub_form}
    return render(request, 'core/underCostruction.html', context)

#MODIFIED

class HomeView(ListView):
    queryset = Casa.objects.all()
    template_name = 'core/index.html'
    context_object_name = "lista_case"

#pagina del profilo utente
def userProfileView(request, pk):
    user = get_object_or_404(User, pk=pk)
    context = {"user": user}
    return render(request, 'core/user_profile.html', context)

def ModifyProfileView(request, owner):
    if request.method == "POST":
        if owner == "profile":
            profile_form = ProfileForm(request.POST,
                                       request.FILES,
                                       instance=request.user.profile)
        else:
            profile_form = ProfileFormP(request.POST,
                                       instance=request.user.profilep)
        user_form = UpdateFormRegistrazione(request.POST, instance=request.user)
        if user_form.is_valid() and profile_form.is_valid():
            profile_form.save()
            user_form.save()
            return HttpResponseRedirect('/')
        else:
            print("modifica profilo non valida")

    user_form = UpdateFormRegistrazione()
    if owner == "profile":
        profile_form = ProfileForm()
    else:
        profile_form = ProfileFormP()

    context = {"u_form": user_form, "p_form": profile_form}
    return render(request, 'core/modify_profile.html', context)

def thunderCasa(request):
    casaT = get_object_or_404(Casa, id=request.POST.get('casa_id'))
    if request.user.is_authenticated:
        is_thunders = False
        if casaT.thunders.filter(id=request.user.id).exists():
            casaT.thunders.remove(request.user)
            is_thunders = False
        else:
            casaT.thunders.add(request.user)
            is_thunders = True
        return HttpResponseRedirect("/search/?q1=milano&q2=")
    else:
        return HttpResponseRedirect("/search/?q1=milano&q2=")

#n.b. ereditarietà : Userlist eredità da ListView
def ownerHomeView(request, pk):
    user = get_object_or_404(User, pk=pk)
    casa = user.profilep.owners.all()
    print(user.profilep.owners.all())
    conta_case = len(casa)
    context = {"user": user, "lista_case": casa, "conta_case": conta_case}
    return render(request, 'core/case_owner.html', context)

def myHomeView(request, pk):
    user = get_object_or_404(User, pk=pk)
    casa = user.thunders.all()
    conta_case = len(casa)

    casalike = {}
    for c in Casa.objects.all():
        l = len(c.thunders.all())
        if l > 0 :
            print("casa",c.thunders.all())
            casalike[c] = c.thunders.all()

    context = {"user": user, "lista_case": casa, "conta_case": conta_case, "casalike": casalike}
    return render(request, 'category-2-rooms.html', context)

def searchView(request):
    #filtro prezzo
    if "q1" and "q2" in request.GET:
        querystring1 = request.GET.get("q1")
        querystring2 = request.GET.get("q2")
        if len(querystring1) == 0 :
            return redirect("/search/")
        citta = Casa.objects.filter(citta__icontains=querystring1)
        print("citta",citta)
        zona = Casa.objects.filter(zona__icontains=querystring2)
        print("zona",zona)
        if querystring2 == "Tutte":
            lista_case = citta
        elif len(querystring2) != 0:
            lista_case = citta and zona
        else:
            lista_case = citta
        context = {"lista_case": lista_case}
        print("lista_case",lista_case)
        return render(request, 'core/search.html', context)
    else:
        return render(request, 'core/search.html')
