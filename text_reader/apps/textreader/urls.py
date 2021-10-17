# -*- coding: utf-8 -*-
from django.urls import path

from text_reader.apps.textreader import views

app_name = 'textreader'


urlpatterns = [
    path('documents/', views.documents_view, name='view_documents'),
]
