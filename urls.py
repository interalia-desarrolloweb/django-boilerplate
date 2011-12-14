# -*- coding: utf-8 -*-

"""
    Defaults url config
    Author  :   Alvaro Lizama Molina <alvaro.lizama@interalia.net>
"""

from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

from settings import LOCAL, MEDIA_ROOT


admin.autodiscover()

urlpatterns = patterns('',
        url(r'^/admin/$', include('admin.site.urls')),
        url(r'^/admintools/$', include('admin_tools.urls')),
        url(r'^$', include('main.urls')),
        )

if LOCAL:
    urlpatterns += patterns('',
            (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                'document_root': MEDIA_ROOT,
                }),
            )


