from django.views.static import *
from django.conf import settings
from django.conf.urls import patterns, include, url
from mysite.views import hello, homepage, current_datetime, login

urlpatterns = patterns('',
   ('^hello/$', hello),
   ('^$', homepage),
   ('^time/$', current_datetime),
   ('^login/$', homepage),
   (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
   """(r'^logout/$', logout),"""
)
