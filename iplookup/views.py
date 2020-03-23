from django.http import HttpResponse
from iplookup.ipsearch import RBLSearch
from iplookup.models import Rbl, Ip
from django.shortcuts import render
import json


def IpIndexView(request):
    return render(request, 'iplookup/ipindex.html')


def IpLookupView(request, ip):
    context = {"ip": ip}
    return render(request, 'iplookup/iplookup.html', context)


def IpBlackListView(request, ip, rbladdress):
    searcher = RBLSearch(ip, [rbladdress])
    json_pretty = searcher.json_results()

    return HttpResponse(json.dumps(json_pretty),
                        content_type="application/json")


def IpAllBlackListView(request, ip):
    result = Rbl.objects.filter(active=True)
    RBLS = [entry.address for entry in result]
    searcher = RBLSearch(ip, RBLS)
    json_pretty = searcher.json_results()

    return HttpResponse(json.dumps(json_pretty),
                        content_type="application/json")


def AllIpAllBlackListView(request):
    ipresult = Ip.objects.filter(active=True)
    IPS = [entry.ipaddress for entry in ipresult]

    rblresult = Rbl.objects.filter(active=True)
    RBLS = [entry.address for entry in rblresult]

    list_result = []
    if IPS:
        for ip in IPS:
            searcher = RBLSearch(ip, RBLS)
            list_result.append(searcher.json_results())
    else:
        list_result = {'ERROR': True}
    # print(list_result)
    return HttpResponse(json.dumps(list_result),
                        content_type="application/json")


def BlackListIndexView(request, ip):
    context = {"ip": ip}
    return render(request, 'iplookup/iplookup_blacklist.html', context)


###############################################################################
def FcrdnsIndexView(request, ip):
    context = {"ip": ip}
    return render(request, 'iplookup/iplookup_blacklist.html', context)


def WhoisIndexView(request, ip):
    context = {"ip": ip}
    return render(request, 'iplookup/iplookup_blacklist.html', context)


def DmarcIndexView(request, ip):
    context = {"ip": ip}
    return render(request, 'iplookup/iplookup_blacklist.html', context)
