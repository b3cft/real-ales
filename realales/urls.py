from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^beer/', include('beer.urls')),
    (r'^brewery/', include('brewery.urls')),
    (r'^admin/', include(admin.site.urls)),
)
