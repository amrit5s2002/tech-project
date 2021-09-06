from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('' , views.home , name='project' ),
    path('bchain.html' , views.bchain , name = 'bchain'),
    path('ar.html' , views.ar , name = 'ar'),
    path('nlp.html' , views.nlp , name = 'nlp')
]