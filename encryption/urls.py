from django.urls import path
from . import views
from django.contrib import messages
from django.shortcuts import redirect

app_name = 'encryption'
urlpatterns = [
    path('', views.index, name='index'),
    #path('encryption', views.encryption, name='encryption'),
    path('mydrive', views.mydrive, name='mydrive'),
    path('download/<str:file_content>', views.download, name='download'),
    path('send/<str:file_content>', views.send, name='send'),
    path('delete/<str:file_content>', views.delete, name='delete'),
]