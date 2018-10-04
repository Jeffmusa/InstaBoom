from django.shortcuts import render
import datetime as dt
from .models import *
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    date = dt.date.today()
    return render(request, 'home.html',{"date": date,})