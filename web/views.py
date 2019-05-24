# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse
import json
# Create your views here.


def index(request):
    data = {}
    remote_addr = request.META['REMOTE_ADDR']
    data['remote_addr'] = remote_addr
    if request.META.has_key('HTTP_X_FORWARDED_FOR'):
        http_x_forward_for = request.META['HTTP_X_FORWARDED_FOR']
        data['http_x_forward_for'] = http_x_forward_for

    data = json.dumps(data)
    return HttpResponse(data)
