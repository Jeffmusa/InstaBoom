from django.shortcuts import render
import datetime as dt
from django.http  import HttpResponse

# Create your views here.
def welcome(request):
    date = dt.date.today()
    return render(request, 'home.html',{"date": date,})