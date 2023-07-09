from django.urls import path
from . import views
from django.contrib import messages
from django.shortcuts import redirect

app_name = 'py'
urlpatterns = [
    path('', views.index, name='index'),
    #path('encryption', views.encryption, name='encryption'),

]