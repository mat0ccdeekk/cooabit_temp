from braces.views import LoginRequiredMixin
from django.views import generic
from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404, redirect
from .forms import FormZoom

# class UserListView(LoginRequiredMixin, generic.ListView):
#     model = get_user_model()
#     # These next two lines tell the view to index lookups by username
#     slug_field = 'username'
#     slug_url_kwarg = 'username'
#     template_name = 'custom_app/users.html'
#     login_url = 'admin/'


User = get_user_model()
def confermaArrivata(request):
    return render(request, 'custom_app/confermaAccordo.html')



def index(request, pk):
    user = get_object_or_404(User, pk=pk)
    mieCase = user.thunders.all()
    listaU = []

    # print("mie case",mieCase)
    utenti = {}
    sID = ""
    for c in mieCase:
        for u in c.thunders.all():
            if user != u:
                listaU.append(u)
        if listaU == []:
            continue
        else:
            utenti[c] = listaU
            listaU = []

    # print("coSinqulini ",utenti)

    if request.method == "POST":
        form = FormZoom(request.POST)
        if form.is_valid():
            form.save()
            print(form)
            return redirect('conferma')
        else:
            print("oooops ncuna cosa non funziona va trovala")
            print(form)
    form = FormZoom()

    context = {"user": user, "lista_case": mieCase, "utenti": utenti, "form": form}
    return render(request, 'custom_app/index.html', context)

#
# def confermaZoom(request):
#     if request.method == "POST":
#         form = FormZoom(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#         else:
#             print("oooops ncuna cosa non funziona va trovala")
#
#     form = FormZoom()
#     context = {"form": form}
#     return render(request, 'custom_app/index.html', context)


#
# def index(request, pk):
#     user = get_object_or_404(User, pk=pk)
#     mieCase = user.thunders.all()
#
#     print("mie case",mieCase)
#     dUtente = {}
#     sID = ""
#     for c in mieCase:
#         for roomM in c.thunders.all():
#             if user != roomM:
#                 sID = roomM.email+"@"+user.email
#                 l = sID.split("@")
#                 l.sort()
#                 st = "".join(l)
#                 st = st.replace(".","w")
#                 s1 = ""
#                 for i in range(0, len(st)):
#                     num = ord(st[i])+1
#                     s = chr(num)
#                     s1 += s
#                 dUtente[roomM.id] = [roomM.first_name+" "+roomM.last_name, s1]
#     print(dUtente)
#
#     context = {"user": user, "lista_case": mieCase, "d_utente": dUtente}
#     return render(request, 'custom_app/index.html', context)
