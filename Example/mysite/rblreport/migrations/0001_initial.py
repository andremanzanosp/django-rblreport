# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('IpAddr', models.GenericIPAddressField(unique=True, verbose_name=b'Ip address')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pool',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('PoolName', models.CharField(unique=True, max_length=50, verbose_name=b'Pool name')),
                ('SendAlert', models.BooleanField(default=False, verbose_name=b'Send Alert?')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rbl',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('RblName', models.CharField(unique=True, max_length=100, verbose_name=b'Rbl name')),
                ('RblAddr', models.CharField(unique=True, max_length=100, verbose_name=b'Rbl address')),
                ('RblLink', models.CharField(max_length=200, null=True, verbose_name=b'Rbl link')),
                ('SendAlert', models.BooleanField(default=False, verbose_name=b'Send Alert?')),
                ('RblProto', models.CharField(default=b'd', max_length=1, verbose_name=b'Used Protocol', choices=[(b'd', b'DNS'), (b'h', b'HTTP')])),
                ('RblProtoExtra', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RblRcode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('RcodeName', models.CharField(max_length=50, verbose_name=b'Return code')),
                ('Status', models.CharField(default=b'C', max_length=1, verbose_name=b'Return status', choices=[(b'C', b'CRITICAL'), (b'W', b'WARNING'), (b'N', b'NORMAL'), (b'U', b'UNKNOWN')])),
                ('Extra', models.CharField(max_length=200, null=True, blank=True)),
                ('ExtraLink', models.CharField(max_length=200, null=True, blank=True)),
                ('rbl', models.ForeignKey(to='rblreport.Rbl')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ServerName', models.CharField(unique=True, max_length=50, verbose_name=b'Server name')),
                ('pool', models.ForeignKey(to='rblreport.Pool')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StatusHistoric',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Date', models.DateTimeField(auto_now_add=True)),
                ('Last', models.BooleanField(default=True)),
                ('ip', models.ForeignKey(to='rblreport.Ip')),
                ('rblrcode', models.ForeignKey(to='rblreport.RblRcode')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('UnitName', models.CharField(unique=True, max_length=50, verbose_name=b'Unit name')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='pool',
            name='unit',
            field=models.ForeignKey(to='rblreport.Unit'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ip',
            name='server',
            field=models.ForeignKey(to='rblreport.Server'),
            preserve_default=True,
        ),
    ]
