from django.conf.urls import patterns, include, url
from views import not_found, test

urlpatterns = patterns('',
    url(r'^/$', not_found),
    url(r'^login/$', not_found),
    url(r'^signup/$', not_found),
    url(r'^ask/$', not_found),
    url(r'^popular/$', not_found),
    url(r'^new/$', not_found),
    url(r'^question/(.+)/$', test),
)
