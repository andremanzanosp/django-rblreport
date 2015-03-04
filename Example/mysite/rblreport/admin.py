from django.contrib import admin
from rblreport.models import Unit, Pool, Server, Ip, Rbl, RblRcode, StatusHistoric

class IpAdmin(admin.ModelAdmin):
    '''
    Class used by django to create Admin (CRUD) for Ip table
    '''
    list_display   = ('IpAddr', 'server')
    search_fields  = ['IpAddr']

class IpInline(admin.TabularInline):
    '''
    Class used by django to include Ip into Server Admin
    '''
    model = Ip

class ServerAdmin(admin.ModelAdmin):
    '''
    Class used by django to create Admin (CRUD) for Server table
    '''
    list_display   = ('ServerName', 'pool')
    search_fields  = ['ServerName']
    inlines = [
        IpInline,
    ]

class PoolAdmin(admin.ModelAdmin):
    '''
    Class used by django to create Admin (CRUD) for Pool table
    '''
    list_display   = ('PoolName', 'unit', 'SendAlert')
    search_fields  = ['PoolName']

class UnitAdmin(admin.ModelAdmin):
    '''
    Class used by django to create Admin (CRUD) for Unit table
    '''
    search_fields  = ['UnitName']


class RblAdmin(admin.ModelAdmin):
    '''
    Class used by django to create Admin (CRUD) for Rbl table
    '''
    list_display   = ('RblName', 'SendAlert', 'RblAddr', 'RblProto', 'RblProtoExtra', 'RblLink')
    search_fields  = ['RblAddr']

class RblRcodeAdmin(admin.ModelAdmin):
    '''
    Class used by django to create Admin (CRUD) for "Rbl Return Code" table
    '''
    list_display   = ('RcodeName', 'rbl', 'Status', 'Extra', 'ExtraLink')
    search_fields  = ['RcodeName']

class StatusHistoricAdmin(admin.ModelAdmin):
    '''
    Class used by django to create Admin (CRUD) for "Status Historic" table
    '''
    list_display   = ('ip', 'rblrcode', 'Last', 'Date')
#    date_hierarchy = 'Date'
    list_filter    = ['Date']

admin.site.register(Unit, UnitAdmin)
admin.site.register(Pool, PoolAdmin)
admin.site.register(Server, ServerAdmin)
admin.site.register(Ip, IpAdmin)
admin.site.register(Rbl, RblAdmin)
admin.site.register(RblRcode, RblRcodeAdmin)
admin.site.register(StatusHistoric, StatusHistoricAdmin)
