from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
import os

from my_files.models import Files

from django.http import FileResponse
def file_down(request,filename=None):
    path=os.path.join(os.path.join(os.getcwd(),'my_files/files'),filename)
    print(path)
    file=open(path,'rb')
    response =FileResponse(file)
    response['Content-Type']='application/octet-stream'
    response['Content-Disposition']='attachment;filename=%s' % filename
    return response



@csrf_exempt
def files(request,down_file=None):
    files = Files.objects.all().values_list('name').distinct()
    files = [i[0] for i in files]
    if request.method == 'POST':
        file = request.FILES.get('myfile')
        if not file:
            return render(request, 'my_files/files.html', {'files':files,'msg': '没有上传文件'})
        recv_file = os.path.join(os.path.join(os.getcwd(), r'my_files/files'), file.name)
        with open(recv_file, 'wb+') as f:
            for chunk in file.chunks():
                f.write(chunk)
        Files.objects.create(name=file.name)
    if down_file:
        return file_down(request,down_file)

    return render(request, 'my_files/files.html',{'files':files,})
