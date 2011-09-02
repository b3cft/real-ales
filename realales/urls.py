from django.conf.urls.defaults import include, patterns, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'pages.views.home', name='homepage'),                   
    (r'^search/', include('search.urls')),                   
    (r'^beer/', include('beer.urls')),
    (r'^brewery/', include('brewery.urls')),
    (r'^admin/', include(admin.site.urls)),
)
