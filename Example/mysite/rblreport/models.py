from django.db import models

class Unit(models.Model):
    ''' 
    Class used to interact with the database
    Table "Unit" keeps the existing units or companies
    An Unit can have many Pools
    '''
    UnitName  = models.CharField(max_length=50, unique=True, verbose_name="Unit name")
    
    def __unicode__(self):
        return self.UnitName


class Pool(models.Model):
    ''' 
    Class used to interact with the database
    Table "Pool" keeps the existing Pools
    Eg. MX, SMTP or relay
    A Pool is associated to a single Unit and can have many Servers
    '''
    unit        = models.ForeignKey(Unit)
    PoolName    = models.CharField(max_length=50, unique=True, verbose_name="Pool name")
    SendAlert   = models.BooleanField(default=False , verbose_name="Send Alert?")

    def __unicode__(self):
        return self.PoolName


class Server(models.Model):
    ''' 
    Class used to interact with the database
    Table "Server" keeps the existing Servers
    A Server is associated to a single Pool and can have many Ips
    '''
    pool       = models.ForeignKey(Pool)
    ServerName = models.CharField(max_length=50, unique=True, verbose_name="Server name")

    def __unicode__(self):
        return self.ServerName


class Ip(models.Model):
    '''
    Class used to interact with the database
    Table "Ip" keeps the existing Ips
    An Ip is associated to a single Server
    '''
    server     = models.ForeignKey(Server)
    IpAddr     = models.GenericIPAddressField(unique=True, verbose_name="Ip address")

    def __unicode__(self):
        return self.IpAddr


class Rbl(models.Model):
    '''
    Class used to interact with the database
    Table "Rbl" keeps the existing Rbls
    A Rbl can have many Return Codes (class: RblRcode)
    '''
    RBL_PROTOCOL_CHOICES = (
        ('d', 'DNS'),
        ('h', 'HTTP'),
    )
    RblName       = models.CharField(max_length=100, unique=True, verbose_name="Rbl name")
    RblAddr       = models.CharField(max_length=100, unique=True, verbose_name="Rbl address")
    RblLink       = models.CharField(max_length=200, null=True, verbose_name="Rbl link")
    SendAlert     = models.BooleanField(default=False , verbose_name="Send Alert?")
    RblProto      = models.CharField(max_length=1, choices=RBL_PROTOCOL_CHOICES, default='d', verbose_name="Used Protocol")
    RblProtoExtra = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.RblName


class RblRcode(models.Model):
    '''
    Class used to interact with the database
    Table "RblRcode" keeps the existing Return Codes for each Rbl
    A Return Code is associated to a single Rbl
    '''
    RCODE_STATUS_CHOICES = (
        ('C', 'CRITICAL'),
        ('W', 'WARNING'),
        ('N', 'NORMAL'),
        ('U', 'UNKNOWN'),
    )
    rbl         = models.ForeignKey(Rbl)
    RcodeName   = models.CharField(max_length=50, verbose_name="Return code")
    Status      = models.CharField(max_length=1, choices=RCODE_STATUS_CHOICES, default='C', verbose_name="Return status")
    Extra       = models.CharField(max_length=200, null=True, blank=True)
    ExtraLink   = models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        retorno = self.RcodeName, self.rbl
        return str(retorno)


class StatusHistoric(models.Model):
    '''
    Class used to interact with the database
    Table "StatusHistoric" keeps the history of every action or blockade existing
    StatusHistoric saves changes of status
    Each Status need an Ip and a RblRcode
    '''
    ip         = models.ForeignKey(Ip)
    rblrcode   = models.ForeignKey(RblRcode)
    Date       = models.DateTimeField(auto_now_add=True)
    Last       = models.BooleanField(default=True)

    def is_last_history(self):
        return 'latest'

    def __unicode__(self):
        retorno = self.ip, self.rblrcode, self.Date
        return str(retorno)


