from django.conf.urls import include,url
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^profile/',views.profile,name = 'profile'),
    url(r'^accounts/',include('registration.backends.simple.urls')),
    url(r'^upload/', views.upload, name='upload'),
]
