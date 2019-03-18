from django.conf.urls import include,url
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^profiles/(\d+)',views.profiles,name='profiles'),
    url(r'^full/(\d+)',views.full,name='full'),
    url(r'^profile/',views.profile,name = 'profile'),
    url(r'^accounts/',include('registration.backends.simple.urls')),
    url(r'^comment/(\d+)',views.comment,name='comment'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^upload/', views.upload, name='upload'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]




if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
