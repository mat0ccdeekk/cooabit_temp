# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    # url(
    #     regex=r'^$',
    #     view=views.UserListView.as_view(),
    #     name='user_list'
    # ),
    path('contatti/<int:pk>/', views.index, name="my_match"),
    path('contatti/conferma/', views.confermaArrivata, name="conferma"),


]
