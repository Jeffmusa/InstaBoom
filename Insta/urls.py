from django.conf.urls import *
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^accounts/',include('registration.backends.simple.urls')),
]
