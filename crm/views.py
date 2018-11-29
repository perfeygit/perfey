from django.shortcuts import render, redirect, HttpResponse, reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def index(request):
    return redirect(reverse('index:index'))