# -*- coding: utf-8 -*-

"""
    Main app url config
    Author  :   Alvaro Lizama Molina <alvaro.lizama@interalia.net>
"""

from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'main.views.index'),
)
