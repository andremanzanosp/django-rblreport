from django.urls import re_path, path
from iplookup import views

app_name = 'iplookup'

urlpatterns = [
    path('', views.IpIndexView, name='IpIndexView'),
    re_path(r'^(?P<ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})/$',
            views.IpLookupView, name='IpLookupView'),
    re_path(r'^(?P<ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})/blacklist/$',
            views.BlackListIndexView, name='BlackListIndexView'),
    re_path(r'^(?P<ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})/blacklist/all/$',
            views.IpAllBlackListView, name='IpAllBlackListView'),
    re_path(r'^(?P<ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})/blacklist/(?P<rbladdress>[a-zA-Z0-9.-_]+)/$',
            views.IpBlackListView, name='IpBlackListView'),
    re_path(r'^all/blacklist/all/$',
            views.AllIpAllBlackListView, name='AllIpAllBlackListView'),

    #######################################################################
    re_path(r'^(?P<ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})/fcrdns/$',
            views.FcrdnsIndexView, name='FcrdnsIndexView'),
    re_path(r'^(?P<ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})/whois/$',
            views.WhoisIndexView, name='WhoisIndexView'),
    re_path(r'^(?P<ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})/dmarc/$',
            views.DmarcIndexView, name='DmarcIndexView'),
]
