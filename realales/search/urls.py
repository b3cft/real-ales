from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'search.views.search', {'phrase':''}),
    url(r'^(?P<phrase>\w+)/$', 'search.views.search', name='search_results'),
)