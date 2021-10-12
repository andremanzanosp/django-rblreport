from django.db import models
from django.utils import timezone


class Ip(models.Model):
    '''
    Class used to interact with the database
    Table "Ip" keeps the existing Ips
    '''
    is_active = models.BooleanField(default=False,
                                    verbose_name="Is Active"
                                    )
    owner = models.ForeignKey('auth.User',
                              related_name='ips',
                              on_delete=models.CASCADE)
    ipaddress = models.GenericIPAddressField(unique=True,
                                             verbose_name="Ip address"
                                             )
    updated = models.DateTimeField(editable=False)
    created = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super(Ip, self).save(*args, **kwargs)

    def __str__(self):
        return self.ipaddress

    class Meta:
        ordering = ['-created']


class Rbl(models.Model):
    '''
    Class used to interact with the database
    Table "Rbl" keeps the existing Blacklists
    '''
    is_active = models.BooleanField(default=False,
                                    verbose_name="Is Active"
                                    )
    name = models.CharField(max_length=100,
                            unique=True,
                            verbose_name="Rbl name",
                            )
    address = models.CharField(max_length=100,
                               unique=True,
                               verbose_name="Rbl address",
                               )
    link = models.CharField(max_length=200,
                            null=True, blank=True,
                            verbose_name="Rbl link"
                            )
    updated = models.DateTimeField(editable=False)
    created = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super(Rbl, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created']


class RblRcode(models.Model):
    '''
    Class used to interact with the database
    Table "RblRcode" keeps the existing Blacklists Return codes
    '''
    code = models.CharField(max_length=100,
                            verbose_name="Rbl Return Code",
                            )
    text = models.CharField(max_length=200,
                            null=True, blank=True,
                            verbose_name="Rbl Return Code text"
                            )
    rbl = models.ForeignKey(Rbl, on_delete=models.CASCADE)

    def __str__(self):
        return self.code


class IpRblHistoric(models.Model):
    '''
    Class used to interact with the database
    Table "IpRblHistoric" keeps the existing Historic of Ip searches on RBLs
    '''
    ip = models.ForeignKey(Ip, on_delete=models.CASCADE)
    rblrcode = models.ForeignKey(RblRcode, on_delete=models.CASCADE)
    listed = models.BooleanField(default=False)
    ttl = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        return super(IpRblHistoric, self).save(*args, **kwargs)

    def __str__(self):
        return "{}/{}/{}".format(self.ip, self.rblrcode, self.listed)

    class Meta:
        ordering = ['-created']


# {
#    "SEARCH_HOST":"127.0.0.2",
#    "DATE_TIME":"2020-04-13T23:11:06-0300",
#    "zen.spamhaus.org":{
#       "LISTED":true,
#       "METADATA":{
#          "NS":[
#             "72.32.19.62",
#             "45.77.193.2"
#          ]
#       },
#       "RCODE":[
#          "127.0.0.2",
#          "127.0.0.10",
#          "127.0.0.4"
#       ],
#       "ERROR":false,
#       "TTL":60,
#       "TEXT":[
#          "https://www.spamhaus.org/sbl/query/SBL2",
#          "https://www.spamhaus.org/query/ip/127.0.0.2"
#       ]
#    }
# }