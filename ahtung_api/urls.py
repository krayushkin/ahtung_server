from django.conf.urls import patterns, include, url
from django.contrib import admin

from ahtung_api.views import ApiView, PopulateView

urlpatterns = patterns('',
        url(r'populate$', PopulateView.as_view()),
		url(r'(?P<action>.*)$', ApiView.as_view()),
        

    # Examples:
    # url(r'^$', 'ahtung_server.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
)
