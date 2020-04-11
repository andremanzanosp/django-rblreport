# from django.shortcuts import render
from rest_framework import viewsets
from .models import Ip, Rbl
from .serializers import IpSerializer, RblSerializer


class IpViewSet(viewsets.ModelViewSet):
    queryset = Ip.objects.all().order_by('id')
    serializer_class = IpSerializer


class RblViewSet(viewsets.ModelViewSet):
    queryset = Rbl.objects.all().order_by('id')
    serializer_class = RblSerializer
