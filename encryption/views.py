import os
import sys
import hashlib
import io
import shutil
import urllib.parse
from .models import enfile
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
    return render(request, 'encryption/index.html')


#def encryption(request):
 #   return render(request, 'encryption/encryption.html')

def mydrive(request):
    result = ""
    if request.method == 'POST':
        f_text = request.POST['text']
        file = request.FILES.get('fileinput')

        if not file:
            return redirect('encryption:index')

        user_directory_path = os.path.join(settings.MEDIA_ROOT, str(request.user.username))
        if not os.path.exists(user_directory_path):
            os.makedirs(user_directory_path)
        file_path = os.path.join(user_directory_path, file.name)

        file_name_parts = os.path.splitext(file.name)
        file_names = os.listdir(user_directory_path) 

        if file_name_parts[1] != ".zip":
            result = 'not zip'
            content = {'result': result}
            return render(request, 'encryption/index.html', content)
        
        for i in range(len(file_names)):
            if file_names[i] == file.name:
                result = 'aleady file'
                content = {'result': result}
                return render(request, 'encryption/index.html', content)

        if not result:
            with open(file_path, "wb") as f:
                f.write(file.read())
            result = 'success upload'
                    
            e = enfile(user_id_id=request.user.id, file_text=f_text, file_content=file.name)
            e.save()

    enlist = enfile.objects.filter(user_id=request.user.id)
    content = {'result': result, 'enlist': enlist}
    return render(request, 'encryption/mydrive.html', content)

def download(request, file_content):
    user_directory_path = os.path.join(settings.MEDIA_ROOT, str(request.user.username))

    if file_content in os.listdir(user_directory_path):
        fs = FileSystemStorage(user_directory_path)
        response = FileResponse(fs.open(file_content, 'rb'))
        file_name = str(file_content)
        response['Content-Disposition'] =  'attachment; filename="{}"'.format(file_name)
        return response

    return redirect('encryption:mydrive')

def send(request, file_content):
    send_name = request.GET['sendid']
    send_id = None
    user_list = User.objects.all()
    for u in user_list:
        if u.username == send_name:
            send_id = u.id
            break
    file = enfile.objects.get(user_id=request.user.id, file_content=file_content)
    file_path = os.path.join(settings.MEDIA_ROOT, str(request.user.username), str(file_content))
    send_path = os.path.join(settings.MEDIA_ROOT, str(send_name), str(file_content))
    
    if not send_name:
        result = 'not input'
    elif not send_id:
        result = 'not id'
    elif os.path.isfile(send_path):
        result = 'aleady file'
    else:
        shutil.copyfile(file_path, send_path)

        e = enfile(user_id_id=send_id, file_text=file.file_text, file_content=file_content, send_user=request.user.username)
        e.save()
        result = 'success send'

    enlist = enfile.objects.filter(user_id=request.user.id)
    content = {'result': result, 'enlist': enlist}
    return render(request, 'encryption/mydrive.html', content)

def delete(request, file_content):
    user_directory_path = os.path.join(settings.MEDIA_ROOT, str(request.user.username))

    if file_content in os.listdir(user_directory_path):
        os.remove(os.path.join(user_directory_path, file_content))

    data = enfile.objects.get(user_id=request.user.id, file_content=file_content)
    data.delete()

    return redirect('encryption:mydrive')

class myAES():
    def __init__(self, keytext, ivtext):
        hash = SHA.new()
        hash.update(keytext.encode('utf-8'))
        key = hash.digest()
        self.key = key[:16]
        hash.update(ivtext.encode('utf-8'))
        iv = hash.digest()
        self.iv = iv[:16]

    def makeEnabled(self, plaintext):
        fillersize = 0
        textsize = len(plaintext)
        if textsize % 16 != 0:
            fillersize = 16 - textsize % 16
        filler = '0' * fillersize
        header = '%d' % (fillersize)
        gap = 16 - len(header)
        header += '#' * gap
        return header + plaintext + filler

    def enc(self, plaintext):
        a = plaintext
        me = sys.getsizeof(a)
        ik = 1
        while True:
            if ik - me >= 16:
                break
            else:
                ik += 16
        p = int((ik - me) % 16)
        list = [b'0', b'1', b'2', b'3', b'4', b'5', b'6', b'7', b'8', b'9', b'10', b'11', b'12', b'13', b'14', b'15']
        if p < 10:
            a = list[p] + b'###############' + a
        else:
            a = list[p] + b'##############' + a

        for i in range(p):
            a += b'0'
        aes = AES.new(self.key, AES.MODE_CBC, self.iv)
        encmsg = aes.encrypt(a)
        return encmsg

    def dec(self, ciphertext):
        aes = AES.new(self.key, AES.MODE_CBC, self.iv)
        decmsg = aes.decrypt(ciphertext)
        header = decmsg[:16].decode()
        fillersize = int(header.split('#')[0])
        if fillersize != 0:
            decmsg = decmsg[16:-fillersize]
        else:
            decmsg = decmsg[16:]
        return decmsg
