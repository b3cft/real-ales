from django.conf.urls.defaults import include, patterns
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'pages.views.home'),                   
    (r'^search/', include('search.urls')),                   
    (r'^beer/', include('beer.urls')),
    (r'^brewery/', include('brewery.urls')),
    (r'^admin/', include(admin.site.urls)),
)
