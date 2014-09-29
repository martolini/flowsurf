from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'flowsurf.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'flowsurf.landing.views.landing', name='landing'),
    url(r'^ajax/subscribe/$', 'flowsurf.landing.views.ajax_landing'),
    url(r'^admin/', include(admin.site.urls)),
)
