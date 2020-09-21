from django.shortcuts import render
from core.forms import SubscriptionForm
from django.http import HttpResponseRedirect
from django.contrib import messages



# Create your views here.

def paySubscriptionView(request):
    if request.method == "POST":
        sub_form = SubscriptionForm(request.POST)
        print(sub_form)
        if sub_form.is_valid():
            sub_form.save()
            messages.add_message(request, messages.SUCCESS, 'Grazie di vero cuore')
        else:
            print("form not validddddd")

    sub_form = SubscriptionForm()
    context = {"sub_form": sub_form}
    return render(request, 'pay/pay_subscription.html', context)
