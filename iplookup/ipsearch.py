#!/usr/bin/env python3

import json
import re
import ipaddress
from dns.resolver import Resolver, NXDOMAIN, NoNameservers, Timeout, NoAnswer
from threading import Thread
from datetime import datetime
from pytz import timezone


class DNSLookup(Thread):
    def __init__(self, host, dnslist, listed):
        Thread.__init__(self)
        self.host = host
        self.listed = listed
        self.dnslist = dnslist
        self.resolver = Resolver()
        self.resolver.timeout = 1.0
        self.resolver.lifetime = 1.5
        self.nameservers = self.resolver.nameservers

    def run(self):
        self.getTwoNameServers()
        if self.nameservers:
            self.resolver.nameservers = self.nameservers

        self.listed[self.dnslist]['METADATA'] = {}
        self.listed[self.dnslist]['METADATA']['NS'] = self.nameservers
        self.listed[self.dnslist]['RCODE'] = []
        host_record = self.DNSQuery(self.host, 'A')
        if host_record['ERROR']:
            self.listed[self.dnslist]['ERROR'] = True
            self.listed[self.dnslist]['ERRORTYPE'] = host_record['ERRORTYPE']
        else:
            self.listed[self.dnslist]['ERROR'] = False
            self.listed[self.dnslist]['LISTED'] = True
            self.listed[self.dnslist]['TTL'] = host_record['TTL']
            for rcode in host_record['RESPONSE']:
                self.listed[self.dnslist]['RCODE'].append(rcode.address)
            self.listed[self.dnslist]['TEXT'] = []

            host_record = self.DNSQuery(self.host, 'TXT')
            if not host_record['ERROR']:
                for rcode in host_record['RESPONSE']:
                    for rcode_uniq in rcode.strings:
                        self.listed[self.dnslist]['TEXT'].append(
                            rcode_uniq.decode("utf-8"))

    def DNSQuery(self, domain, query_type):
        try:
            dns_response = {}
            dnsr = self.resolver.query(domain, query_type)
            dns_response['RESPONSE'] = dnsr
            dns_response['TTL'] = dnsr.rrset.ttl
            dns_response['ERROR'] = False
        except NXDOMAIN:
            dns_response['ERROR'] = True
            dns_response['ERRORTYPE'] = 'NXDOMAIN'
        except NoNameservers:
            dns_response['ERROR'] = True
            dns_response['ERRORTYPE'] = 'NoNameservers'
        except Timeout:
            dns_response['ERROR'] = True
            dns_response['ERRORTYPE'] = 'Timeout'
        except NameError:
            dns_response['ERROR'] = True
            dns_response['ERRORTYPE'] = 'NameError'
        except NoAnswer:
            dns_response['ERROR'] = True
            dns_response['ERRORTYPE'] = 'NoAnswer'
        return dns_response

    def getTwoNameServers(self):
        host_record = self.DNSQuery(self.dnslist, 'NS')
        if not host_record['ERROR']:
            self.nameservers = []
            for rcode in host_record['RESPONSE'][:2]:
                host_record = self.DNSQuery(rcode.target, 'A')
                if not host_record['ERROR']:
                    for rcode in host_record['RESPONSE'][:1]:
                        self.nameservers.append(rcode.address)


class RBLSearch(object):
    def __init__(self, lookup_ip, rbl_addresses):
        self.lookup_ip = lookup_ip
        self.lookup_rbls = rbl_addresses
        self._listed = None

    def getIpReversed(self):
        ip = ipaddress.ip_address(self.lookup_ip)
        ip_reversed = ip.reverse_pointer
        if ip.version == 4:
            ip_reversed = re.sub('.in-addr.arpa', '', ip_reversed)
        elif ip.version == 6:
            ip_reversed = re.sub('.ip6.arpa', '', ip_reversed)
        return ip_reversed

    def search(self):
        if self._listed is None:
            reversed_ip = self.getIpReversed()
            self._listed = {'SEARCH_HOST': self.lookup_ip}
            self._listed['DATE_TIME'] = datetime.now(
                timezone('America/Sao_Paulo')).strftime("%Y-%m-%dT%H:%M:%S%z")
            threads = []
            for rbl in self.lookup_rbls:
                self._listed[rbl] = {'LISTED': False}
                query = DNSLookup("%s.%s" % (reversed_ip, rbl),
                                  rbl,
                                  self._listed
                                  )
                threads.append(query)
                query.start()
            for thread in threads:
                thread.join()
        return self._listed
    listed = property(search)

    def json_results(self):
        return self.listed

    def print_json(self):
        print(json.dumps(self.listed))
