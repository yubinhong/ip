# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import HttpResponse
import json
# Create your views here.


def index(request):
    data = {}
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        http_x_forward_for = request.META['HTTP_X_FORWARDED_FOR']
        data['ip'] = http_x_forward_for
    else:
        data['ip'] = request.META['REMOTE_ADDR']

    data = json.dumps(data)
    return HttpResponse(data)
