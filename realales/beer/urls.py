from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from beer.models import Beer

urlpatterns = patterns('',
    (r'^$',ListView.as_view(queryset=Beer.objects.order_by('name')[:25],template_name='beer/list.html')),
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Beer,
            template_name='beer/detail.html'),
        name='beer_detail'),
)