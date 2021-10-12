from django.contrib import admin
from .models import Ip, Rbl, RblRcode, IpRblHistoric


class IpAdmin(admin.ModelAdmin):
    '''
    Class used by django to create Admin (CRUD) for Ip table
    '''
    # date_hierarchy = 'pub_date'
    list_display = ('ipaddress', 'is_active', 'owner', 'updated', 'created')
    search_fields = ['ipaddress']


class RblAdmin(admin.ModelAdmin):
    '''
    Class used by django to create Admin (CRUD) for Rbl table
    '''
    list_display = ('name', 'address', 'link', 'is_active', 'updated', 'created')
    search_fields = ['address']


class RblRcodeAdmin(admin.ModelAdmin):
    '''
    Class used by django to create Admin (CRUD) for RblRcode table
    '''
    list_display = ('code', 'text', 'rbl')
    search_fields = ['code']


class IpRblHistoricAdmin(admin.ModelAdmin):
    '''
    Class used by django to create Admin (CRUD) for IpRblHistoric table
    '''
    list_display = ('ip', 'rblrcode', 'listed', 'ttl', 'created')
    search_fields = ['ip']


admin.site.register(Ip, IpAdmin)
admin.site.register(Rbl, RblAdmin)
admin.site.register(RblRcode, RblRcodeAdmin)
admin.site.register(IpRblHistoric, IpRblHistoricAdmin)
