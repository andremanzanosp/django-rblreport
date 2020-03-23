from django.db import models


class Rbl(models.Model):
    '''
    Class used to interact with the database
    Table "Rbl" keeps the existing Blacklists
    '''
    active = models.BooleanField(default=False,
                                 verbose_name="Active"
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
                            null=True,
                            verbose_name="Rbl link"
                            )

    def __str__(self):
        return self.name

    def is_active(self):
        return self.active



class Ip(models.Model):
    '''
    Class used to interact with the database
    Table "Ip" keeps the existing Ips
    '''
    active = models.BooleanField(default=False,
                                 verbose_name="Active"
                                 )
    ipaddress = models.GenericIPAddressField(unique=True,
                                             verbose_name="Ip address"
                                             )

    def __str__(self):
        return self.ipaddress



# class StatusHistoric(models.Model):
#     ip = models.ForeignKey(Ip)
#     rbl = models.ForeignKey(Rbl)
#     date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         retorno = self.ip, self.rbl, self.date
#         return str(retorno)
