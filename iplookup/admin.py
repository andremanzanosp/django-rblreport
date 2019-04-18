from django.contrib import admin
from iplookup.models import Rbl


class RblAdmin(admin.ModelAdmin):
    '''
    Class used by django to create Admin (CRUD) for Rbl table
    '''
    list_display = ('name', 'address', 'link', 'active')
    search_fields = ['address']


admin.site.register(Rbl, RblAdmin)
