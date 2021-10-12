from rest_framework import serializers
from .models import Ip, Rbl

from django.contrib.auth.models import User


# Serializers define the API representation.
class IpSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Ip
        fields = ['url', 'id', 'is_active', 'ipaddress', 'owner', 'updated', 'created']


class RblSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rbl
        fields = ['url', 'id', 'is_active',
                  'name', 'address', 'link', 'updated', 'created']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # ips = serializers.PrimaryKeyRelatedField(many=True,
    #                                          queryset=Ip.objects.all())
    ips = serializers.HyperlinkedRelatedField(many=True,
                                              view_name='ip-detail',
                                              read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'ips']
