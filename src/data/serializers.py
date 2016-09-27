from rest_framework import serializers
from data.models import Transactions
from objects.serializers import ObjectSerializer


class TransactionsSerializer(serializers.ModelSerializer):
    object = ObjectSerializer()

    class Meta:
        model = Transactions
        fields = ('id', 'buyer_uuid', 'seller_uuid', 'object', 'state', 'created_at', 'updated_at',)
        read_only_fields = ('id', 'created_at', 'updated_at',)
