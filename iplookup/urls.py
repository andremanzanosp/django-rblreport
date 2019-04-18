from django.urls import re_path
from iplookup import views

app_name = 'iplookup'

urlpatterns = [
    re_path(r'^(?P<Ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})$',
            views.IndexView, name='IndexView'),
    re_path(r'^(?P<Ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})/blacklist/all$',
            views.BlackListAllView, name='BlackListAllView'),
    re_path(r'^(?P<Ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})/blacklist/(?P<rbladdress>[a-zA-Z0-9.]+)',
            views.BlackListView, name='BlackListView'),
    # re_path(r'^(?P<Ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})/(?P<rbladdress>[a-zA-Z0-9.]+)',
    #         views.RblView, name='RblView'),
]
