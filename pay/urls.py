from django.urls import path
from . import views


urlpatterns = [
    path('paySubscription/', views.paySubscriptionView, name="pay_subscription"),

]
