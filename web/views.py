# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import HttpResponse
import json
from backend import ip2Region
from ip import settings
from backend import tools
# Create your views here.


def index(request):
    if request.method == "GET":
        data = {}
        ip_to_region = ip2Region.Ip2Region(settings.ip_data_path)
        if "ip" not in request.GET:
            if 'HTTP_X_FORWARDED_FOR' in request.META:
                http_x_forward_for = request.META['HTTP_X_FORWARDED_FOR']
                real_ip = http_x_forward_for.split(',')[0]
                data['ip'] = real_ip
            else:
                data['ip'] = request.META['REMOTE_ADDR']
        else:
            data['ip'] = request.GET.get('ip')
        if tools.ipv6_check(data['ip']):
            data['region'] = "unknown"
        else:
            data['region'] = ip_to_region.memorySearch(data['ip'])['region']
        data = json.dumps(data).decode('unicode-escape')
        return HttpResponse(data)
    else:
        return HttpResponse("This method is not support.")
