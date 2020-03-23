from django.contrib import admin
from iplookup.models import Rbl, Ip


class RblAdmin(admin.ModelAdmin):
    '''
    Class used by django to create Admin (CRUD) for Rbl table
    '''
    list_display = ('name', 'address', 'link', 'active')
    search_fields = ['address']


class IpAdmin(admin.ModelAdmin):
    '''
    Class used by django to create Admin (CRUD) for Ip table
    '''
    list_display = ('ipaddress', 'active')
    search_fields = ['ipaddress']


admin.site.register(Ip, IpAdmin)
admin.site.register(Rbl, RblAdmin)
