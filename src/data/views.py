# coding=utf-8
from rest_framework import views, status
from .models import Transactions, Object
from .serializers import TransactionsSerializer, TransactionsSerializerCreate, TransactionsSerializerState
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class TransactionDetails(views.APIView):

    @staticmethod
    def get(request, transaction_id):
        serializer_response = TransactionsSerializer(get_object_or_404(Transactions.objects.all(), id=transaction_id))
        return Response(serializer_response.data, status=status.HTTP_200_OK)


class TransactionHistory(views.APIView):

    @staticmethod
    def get(request, user_uuid):
        as_buyer = Transactions.objects.filter(buyer_uuid=user_uuid)
        as_seller = Transactions.objects.filter(seller_uuid=user_uuid)

        serializer_response_as_buyer = TransactionsSerializer(as_buyer, many=True)
        serializer_response_as_seller = TransactionsSerializer(as_seller, many=True)

        return Response({"as_buyer": serializer_response_as_buyer.data,
                         "as_seller": serializer_response_as_seller.data},
                        status=status.HTTP_200_OK)


class CreateTransaction(views.APIView):

    @staticmethod
    def post(request):
        serializer = TransactionsSerializerCreate(data=request.data)

        if serializer.is_valid():
            obj = get_object_or_404(Object.objects.all(), id=serializer.validated_data['object_uuid'])

            trans = Transactions.objects.create(buyer_uuid=serializer.validated_data['buyer_uuid'],
                                                seller_uuid=serializer.validated_data['seller_uuid'],
                                                object=obj,
                                                price=serializer.validated_data['price'],
                                                state=serializer.validated_data['state'])

            serializer_response = TransactionsSerializer(trans)
            return Response(serializer_response.data, status=status.HTTP_201_CREATED)

        return Response({'status': 'Bad request',
                         'message': 'The data that you send is invalid!'},
                        status=status.HTTP_400_BAD_REQUEST)


class UpdateTransactionState(views.APIView):

    @staticmethod
    def post(request):
        serializer = TransactionsSerializerState(data=request.data)

        if serializer.is_valid():
            trans = get_object_or_404(Transactions.objects.all(), id=serializer.validated_data['transaction_id'])
            trans.state = serializer.validated_data['state']
            serializer_response = TransactionsSerializer(trans)
            return Response(serializer_response.data, status=status.HTTP_200_OK)

        return Response({'status': 'Bad request',
                         'message': 'The data that you send is invalid!'},
                        status=status.HTTP_400_BAD_REQUEST)
