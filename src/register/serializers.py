from rest_framework import serializers
from register.models import AppRegister, AppToken


class RegisterAppSerializer(serializers.ModelSerializer):

    class Meta:
        model = AppRegister
        fields = ('name',)
        read_only_fields = ()


class TokenAppSerializer(serializers.ModelSerializer):

    class Meta:
        model = AppToken
        fields = ('token',)
        read_only_fields = ('token',)
