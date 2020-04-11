from django.db import models


class Ip(models.Model):
    '''
    Class used to interact with the database
    Table "Ip" keeps the existing Ips
    '''
    is_active = models.BooleanField(default=False,
                                    verbose_name="Is Active"
                                    )
    ipaddress = models.GenericIPAddressField(unique=True,
                                             verbose_name="Ip address"
                                             )
    # created_date = models.DateTimeField()
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ipaddress


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
                            null=True,
                            verbose_name="Rbl link"
                            )
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# class StatusHistoric(models.Model):
#     ip = models.ForeignKey(Ip)
#     rbl = models.ForeignKey(Rbl)
#     date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         retorno = self.ip, self.rbl, self.date
#         return str(retorno)
