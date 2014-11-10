from django.conf.urls import patterns, include, url
from django.contrib import admin



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ahtung_server.views.home', name='home'),
    url(r'^api/', include('ahtung_api.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
