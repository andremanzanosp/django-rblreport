from django.contrib import admin
from .models import Ip, Rbl


class IpAdmin(admin.ModelAdmin):
    '''
    Class used by django to create Admin (CRUD) for Ip table
    '''
    # date_hierarchy = 'pub_date'
    list_display = ('ipaddress', 'is_active', 'updated_date')
    search_fields = ['ipaddress']


class RblAdmin(admin.ModelAdmin):
    '''
    Class used by django to create Admin (CRUD) for Rbl table
    '''
    list_display = ('name', 'address', 'link', 'is_active', 'updated_date')
    search_fields = ['address']


admin.site.register(Ip, IpAdmin)
admin.site.register(Rbl, RblAdmin)
