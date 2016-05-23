from django.conf.urls import patterns, include, url
from views import main, popular, question, test

urlpatterns = patterns('',
    url(r'^$', main),
    url(r'^login/', test),
    url(r'^signup/', test),
    url(r'^ask/', test),
    url(r'^popular/', popular),
    url(r'^new/', test),
    url(r'^question/(?P<question_id>[0-9]+)/', question, name='question'),
)
