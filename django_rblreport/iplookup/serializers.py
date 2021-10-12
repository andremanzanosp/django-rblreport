from rest_framework import serializers


# class IpLookupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         # model = Ip
#         fields = ['url', 'id', 'is_active', 'ipaddress', 'updated_date']


class IpLookupSerializer(serializers.Serializer):
    # id = serializers.IntegerField(read_only=True)
    ipaddress = serializers.IPAddressField(protocol='IPv4', required=True)

    # def create(self, validated_data):
    #     """
    #     Create and return a new `Snippet` instance, given the validated data.
    #     """
    #     return Snippet.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Snippet` instance,
    #     given the validated data.
    #     """
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.code = validated_data.get('code', instance.code)
    #     instance.linenos = validated_data.get('linenos', instance.linenos)
    #     instance.language = validated_data.get('language', instance.language)
    #     instance.style = validated_data.get('style', instance.style)
    #     instance.save()
    #     return instance
