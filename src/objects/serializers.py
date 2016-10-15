from rest_framework import serializers
from objects.models import Object


class ObjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Object
        fields = ('id', 'name', 'url', 'created_at', 'updated_at',)
        read_only_fields = ('id', 'name', 'url', 'created_at', 'updated_at',)


class ObjectCreateSerializer(serializers.ModelSerializer):
    identifier = serializers.CharField(max_length=128)
    url = serializers.URLField()

    class Meta:
        model = Object
        fields = ('id', 'name', 'url', 'identifier', 'created_at', 'updated_at',)
        read_only_fields = ('id', 'created_at', 'updated_at',)
