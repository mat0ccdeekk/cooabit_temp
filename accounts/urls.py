from django.urls import path
from .views import MandaEmail, RegistrazioneView, RegistrazioneViewP, PrivacyView, ConditionView, ActivateAccountView

urlpatterns = [
    path('registrazione/', RegistrazioneView, name="registrazione_view"),
    path('registrazioneOwner/', RegistrazioneViewP, name="registrazione_view_owner"),
    path('privacy/', PrivacyView, name="privacy_view"),
    path('condition/', ConditionView, name="condition_view"),
    path('activate/<uidb64>/<token>/', ActivateAccountView.as_view(), name="activate"),
    path('email/', MandaEmail, name="manda_email"),


]