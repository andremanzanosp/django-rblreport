from rest_framework import viewsets
from .serializers import IpLookupSerializer
# from iplookup.rbl import RBLSearch

from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView


@permission_classes((permissions.AllowAny,))
class IpLookupView(APIView):
    """
    Ip lookup
    """
    def get_object(self, ip):
        # a = RBLSearch('127.0.0.2', ['dnsbl.sorbs.net'])
        return {'ipaddress': ip}

    def get(self, request, ip, format=None):
        content = self.get_object(ip)
        serializer = IpLookupSerializer(data=content)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes((permissions.AllowAny,))
class IpLookupViewSet(viewsets.ViewSet):
    """
    Ip lookup
    """
    def get_object(self, ip):
        # a = RBLSearch('127.0.0.2', ['dnsbl.sorbs.net'])
        return {'ipaddress': ip}

    def list(self, request, ip, format=None):
    # def detail(self, request, ip, format=None):
        content = self.get_object(ip)
        serializer = IpLookupSerializer(data=content)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
