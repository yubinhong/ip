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
            data['ip'] = request.META['REMOTE_ADDR']
        else:
            data['ip'] = request.GET.get('ip')
        if tools.ipv6_check(data['ip']):
            data['region'] = "unknown"
        else:
            data['region'] = ip_to_region.memorySearch(data['ip'])['region'].decode('utf8')
        data = json.dumps(data).encode("utf-8").decode('unicode-escape')
        return HttpResponse(data)
    else:
        return HttpResponse("This method is not support.")
