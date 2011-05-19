from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from brewery.models import Brewery

urlpatterns = patterns('',
    (r'^$',
        ListView.as_view(
            queryset=Brewery.objects.order_by('name')[:20],
            template_name='brewery/list.html')),
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Brewery,
            template_name='brewery/detail.html'),
        name='brewery_details'),
)