import os
import sys
import hashlib
import io
import shutil
import urllib.parse
from datetime import datetime
from Crypto.Hash import SHA256 as SHA
from Crypto.Cipher import AES
from django.conf import settings
from django.http import FileResponse
from django.http import HttpResponse
from common.forms import UserForm
from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

def index(request):
    return render(request, 'py/cipher.exe')


