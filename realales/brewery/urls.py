from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from brewery.models import Brewery

urlpatterns = patterns('',
    url(r'^$', 'brewery.views.list', 
        name='brewery_list'),
    url(r'^find$', 'brewery.views.list',
        name='brewery_search'),
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Brewery,
            template_name='brewery/detail.html'),
        name='brewery_detail'),
)