
'''from .views import index,download_page,download_exe_file
from django.urls import path

urlpatterns = [
    #path("", download_page, name="download_page"),
    path("", download_page, name="download_page"),
    path('download_exe_file', download_exe_file, name="download_exe_file"),

]
'''
from .views import index,download_page,download_exe_file
from django.urls import path

urlpatterns = [
    #path("", download_page, name="download_page"),
    path("", download_page, name="download_page"),
    path('download/', download_exe_file, name="download_exe_file"),

]



