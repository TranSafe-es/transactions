from rest_framework import serializers
from data.models import Transactions
from objects.serializers import ObjectSerializer


class TransactionsSerializer(serializers.ModelSerializer):
    object = ObjectSerializer()

    class Meta:
        model = Transactions
        fields = ('id', 'buyer_uuid', 'seller_uuid', 'object', 'price', 'state', 'created_at', 'updated_at',)
        read_only_fields = ('id', 'created_at', 'updated_at',)


class TransactionsSerializerCreate(serializers.ModelSerializer):
    object_uuid = serializers.CharField(max_length=128)

    class Meta:
        model = Transactions
        fields = ('buyer_uuid', 'seller_uuid', 'object_uuid', 'price', 'state',)
        read_only_fields = ()


class TransactionsSerializerState(serializers.ModelSerializer):
    transaction_id = serializers.CharField(max_length=128)

    class Meta:
        model = Transactions
        fields = ('state', 'transaction_id')
        read_only_fields = ()
