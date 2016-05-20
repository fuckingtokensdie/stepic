from django.conf.urls import patterns, include, url
from views import not_found, test

urlpatterns = patterns('',
    url(r'^$', test),
    url(r'^login/$', test),
    url(r'^signup/$', test),
    url(r'^ask/$', test),
    url(r'^popular/$', test),
    url(r'^new/$', test),
    url(r'^question/(.+)/$', test),
)
