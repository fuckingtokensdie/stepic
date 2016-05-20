from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^/$', 'views.not_found'),
    url(r'^login/$', 'views.not_found'),
    url(r'^signup/$', 'views.not_found'),
    url(r'^ask/$', 'views.not_found'),
    url(r'^popular/$', 'views.not_found'),
    url(r'^new/$', 'views.not_found'),
    url(r'^question/([0-9]{4})/$', 'views.test'),
)
