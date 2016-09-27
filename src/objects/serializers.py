from rest_framework import serializers
from objects.models import Object
import uuid


class ObjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Object
        fields = ('id', 'name', 'url', 'created_at', 'updated_at',)
        read_only_fields = ('id', 'name', 'url', 'created_at', 'updated_at',)


class ObjectCreateSerializer(serializers.ModelSerializer):
    user_uuid = serializers.CharField(max_length=128)

    class Meta:
        model = Object
        fields = ('id', 'name', 'url', 'user_uuid', 'created_at', 'updated_at',)
        read_only_fields = ('id', 'created_at', 'updated_at',)
