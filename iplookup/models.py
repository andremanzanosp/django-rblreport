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

    def __unicode__(self):
        return self.name

    def is_active(self):
        return self.active
