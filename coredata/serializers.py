from rest_framework import serializers
from .models import Ip, Rbl


# Serializers define the API representation.
class IpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ip
        fields = ['id', 'is_active', 'ipaddress', 'updated_date']


class RblSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rbl
        fields = ['id', 'is_active', 'name', 'address', 'link', 'updated_date']
