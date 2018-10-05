from django.shortcuts import render,redirect
import datetime as dt
from .models import *
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ImageForm

# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    date = dt.date.today()
    return render(request, 'home.html',{"date": date,})


def profile(request):
    date = dt.date.today()
    return render(request, 'profile.html',{"date": date,})


def upload(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('upload')

    else:
        form = ImageForm()
    return render(request, 'upload.html', {"form": form})