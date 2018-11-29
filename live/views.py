from django.shortcuts import render,HttpResponse,redirect

from django.conf import settings
ip=settings.LIVE_IP
# Create your views here.

def index(request):
    return render(request,'live.html',{'ip':ip})