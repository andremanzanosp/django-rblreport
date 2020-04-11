from django.core.management.base import BaseCommand
from iplookup.rbl import RBLSearch
# from coredata.models import Rbl
# import re
import ipaddress


class Command(BaseCommand):
    help = 'Check ip address agaist RBLs'

    def add_arguments(self, parser):
        parser.add_argument('--ips',
                            required=True,
                            nargs='+',
                            help='Internet protocol address [127.0.0.2]')
        parser.add_argument('--rbls',
                            nargs='+',
                            help='Blacklist url [zen.spamhaus.org]')

    def handle(self, *args, **options):
        try:
            for ip in options['ips']:
                ipaddress.ip_address(ip)
            if options['rbls']:
                RBLS = options['rbls']
            # else:
            #     result = Rbl.objects.filter(is_active=True)
            #     RBLS = [entry.address for entry in result]

            searcher = RBLSearch(ip, RBLS)
            searcher.print_json()
        except ValueError:
            print('ERROR: Invalid IPv4: {}'.format(options['ips']))
        except KeyboardInterrupt:
            pass

# python3 manage.py ipsearch --ips 127.0.0.2 --rbls zen.spamhaus.org
