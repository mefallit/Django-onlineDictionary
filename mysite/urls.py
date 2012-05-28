from django.views.static import *
from django.conf import settings
from django.conf.urls import patterns, include, url
from mysite.views import hello, homepage, current_datetime, login, item, register
from dictionary import views

urlpatterns = patterns('',
   ('^login/$', homepage),
   ('^hello/$', hello),
   ('^$', homepage),
   ('^time/$', current_datetime),   
   (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
   ('^item/$', item),
   (r'^item/[a-zA-Z]+/$', item),
   ('^register/$', register),
   (r'^search-form/$', views.search_form),
   (r'^search/$', views.search),
)
