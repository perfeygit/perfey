import os
from django.shortcuts import render, redirect, HttpResponse, reverse
from django.contrib.auth.decorators import login_required
from .stream import stream_video
from pathlib import Path

from django.conf import settings

ip = settings.MEDIA_IP


# Create your views here.
@login_required
def video(request, id):
    path = {
        '1': r'media/static/media/vim.mp4',
        '2': r'media/static/media/1.mp4',
        '3': r'media/static/media/小幸运.mp4',
        '11': r'media/static/media/孤星独吟.mp3',
        '12': r'media/static/media/错过.mp3',
        '13': r'media/static/media/小清新.m4a',
    }
    if id == '0':
        return render(request, 'media/video.html', {"ip": ip})
    path = Path(os.path.join(os.getcwd(), path[id])).as_posix()
    return stream_video(request, path)
