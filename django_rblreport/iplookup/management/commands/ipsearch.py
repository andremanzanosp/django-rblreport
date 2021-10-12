from django.core.management.base import BaseCommand
from iplookup.rbl import RBLSearch
from coredata.models import Ip, Rbl
import ipaddress


class Command(BaseCommand):
    help = 'Check ip address agaist RBLs'

    def add_arguments(self, parser):
        parser.add_argument('--ips',
                            nargs='+',
                            help='Internet protocol address [127.0.0.2]')
        parser.add_argument('--rbls',
                            nargs='+',
                            help='Blacklist url [zen.spamhaus.org]')

    def handle(self, *args, **options):
        try:
            if options['ips']:
                for ip in options['ips']:
                    ipaddress.ip_address(ip)
            else:
                ipresult = Ip.objects.filter(is_active=True)
                options['ips'] = [entry.ipaddress for entry in ipresult]

            if not options['rbls']:
                rblresult = Rbl.objects.filter(is_active=True)
                options['rbls'] = [entry.address for entry in rblresult]

            for ip in options['ips']:
                searcher = RBLSearch(ip, options['rbls'])
                searcher.print_json()
        except ValueError:
            print('ERROR: Invalid IPv4: {}'.format(options['ips']))
        except KeyboardInterrupt:
            pass
