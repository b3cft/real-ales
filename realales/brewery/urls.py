from django.conf.urls.defaults import url, patterns
from django.views.generic import DetailView
from brewery.models import Brewery

urlpatterns = patterns('',
    url(r'^$', 'brewery.views.search', {'phrase':'', 'startswith':False}),
    url(r'^(?P<pk>\d+)/$',DetailView.as_view(model=Brewery, template_name='brewery/detail.html'), name='brewery_detail'),
    url(r'^(?P<phrase>\w+)/$', 'brewery.views.search', {'startswith':False}, name='brewery_list'),
    url(r'^-(?P<phrase>\w+)/$', 'brewery.views.search', {'startswith':True}, name='brewery_startswith'),
)