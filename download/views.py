'''from django.shortcuts import render
from django.http import FileResponse
import os
from django.conf import settings


def index(request):
        return render(request, 'download/download_page.html')




def download_page(request):
    return render(request, 'download/download_page.html')


def download_exe_file(request):
    # 파일 경로
    file_path = os.path.join('C://Users/HANSUNG/Downloads/이력서, 자기소개서 작성 방법.pdf')
    #file_path2 = 'C://Users/HANSUNG/Downloads/이력서, 자기소개서 작성 방법.pdf'
    # 파일 이름
    file_name2 = 'testfile.pdf'
    # 파일을 response로 반환
    response2 = FileResponse(open(file_path2, 'rb'))
    response2['content_type'] = 'application/octet-stream'
    response2['Content-Disposition'] = f'attachment; filename="{file_name2}"'
    return response2
'''

from django.shortcuts import render
from django.http import FileResponse
import os
from django.conf import settings


def index(request):
    return render(request, 'index.html')




def download_page(request):
    return render(request, 'download/download_page.html')


def download_exe_file(request):
    # 파일 경로
    file_path = os.path.join(settings.BASE_DIR, 'templates', 'py', 'cipher.exe')

    # 파일 이름
    file_name = 'cipher.exe'
    # 파일을 response로 반환
    response = FileResponse(open(file_path, 'rb'))
    response['content_type'] = 'application/octet-stream'
    response['Content-Disposition'] = f'attachment; filename="{file_name}"'
    return response
