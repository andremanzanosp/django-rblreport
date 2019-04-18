from django.http import HttpResponse
from iplookup.ipsearch import RBLSearch
from iplookup.models import Rbl


def IndexView(request, Ip):
    return HttpResponse("<html><body><h1>%s</h1><br><br>...</body></html>" % Ip)

def BlackListAllView(request, Ip):
    result = Rbl.objects.filter(active=True)
    RBLS = [entry.address for entry in result]
    searcher = RBLSearch(Ip, RBLS)
    json_pretty = searcher.json_results()

    return HttpResponse(json_pretty, content_type="application/json")


def BlackListView(request, Ip, rbladdress):
    searcher = RBLSearch(Ip, [rbladdress])
    json_pretty = searcher.json_results()

    return HttpResponse(json_pretty, content_type="application/json")
