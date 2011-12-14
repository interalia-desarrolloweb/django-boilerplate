# -*- coding: utf-8 -*-

"""
    Main site controller
    Author  :   Alvaro Lizama Molina <alvaro.lizama@interalia.net>
"""

from django.views.generic.simple import direct_to_template


def index(request):
    data = {'title': 'Boostrap'}
    return direct_to_template(request, 'index.html', data)

