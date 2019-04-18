from django.core.management.base import BaseCommand
from iplookup.ipsearch import RBLSearch
from iplookup.models import Rbl
import re


class Command(BaseCommand):
    help = 'Check ip address agaist RBLs'

    def add_arguments(self, parser):
        parser.add_argument('ip', nargs='+')

    def handle(self, *args, **options):
        '''
        This is the main method that reads data and do stuffs
        '''
        # print(options['ip'])
        try:
            for ip in options['ip']:
                pat = re.compile("\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}")
                is_ip_address = pat.match(ip)
                if is_ip_address:
                    result = Rbl.objects.filter(active=True)
                    RBLS = [entry.address for entry in result]
                    searcher = RBLSearch(ip, RBLS)
                    searcher.print_json()
                else:
                    print("--- NOT an ip address: %s ---" % ip)
        except KeyboardInterrupt:
            pass

