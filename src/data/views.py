# coding=utf-8
from rest_framework import views, status
from .models import Transactions, Object
from .serializers import TransactionsSerializer, TransactionsSerializerCreate, TransactionsSerializerState, \
    TransactionTrackingCode
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from register.permissions import verify_token
from django.db.models import Sum


class TransactionDetails(views.APIView):

    @staticmethod
    def get(request, transaction_id):
        app = verify_token(request)

        serializer_response = TransactionsSerializer(get_object_or_404(Transactions.objects.all(), id=transaction_id,
                                                                       app=app))
        return Response(serializer_response.data, status=status.HTTP_200_OK)


class TransactionsStats(views.APIView):

    @staticmethod
    def get(request):
        return Response({
            "number_of_transactions": Transactions.objects.all().count(),
            "total_value": Transactions.objects.aggregate(Sum('price')),
            "number_of_refunded": Transactions.objects.filter(state="REFUND").count()
        }, status=status.HTTP_200_OK)


class TransactionHistory(views.APIView):

    @staticmethod
    def get(request, identifier):
        app = verify_token(request)

        to_uuid = Transactions.objects.filter(to_uuid=identifier, app=app)
        from_uuid = Transactions.objects.filter(from_uuid=identifier, app=app)

        serializer_response_to_uuid = TransactionsSerializer(to_uuid, many=True)
        serializer_response_from_uuid = TransactionsSerializer(from_uuid, many=True)

        return Response({"to_uuid": serializer_response_to_uuid.data,
                         "from_uuid": serializer_response_from_uuid.data},
                        status=status.HTTP_200_OK)


class TransactionStats(views.APIView):

    @staticmethod
    def get(request, identifier):
        app = verify_token(request)

        to_uuid = Transactions.objects.filter(to_uuid=identifier, app=app)
        from_uuid = Transactions.objects.filter(from_uuid=identifier, app=app)

        serializer_response_to_uuid = TransactionsSerializer(to_uuid, many=True)
        serializer_response_from_uuid = TransactionsSerializer(from_uuid, many=True)

        return Response({"to_uuid": serializer_response_to_uuid.data,
                         "from_uuid": serializer_response_from_uuid.data},
                        status=status.HTTP_200_OK)


class CreateTransaction(views.APIView):

    @staticmethod
    def post(request):
        app = verify_token(request)

        serializer = TransactionsSerializerCreate(data=request.data)

        if serializer.is_valid():
            obj = get_object_or_404(Object.objects.all(), id=serializer.validated_data['object_uuid'], app=app)

            trans = Transactions.objects.create(to_uuid=serializer.validated_data['to_uuid'],
                                                from_uuid=serializer.validated_data['from_uuid'],
                                                object=obj,
                                                price=serializer.validated_data['price'],
                                                state=serializer.validated_data['state'],
                                                app=app)

            serializer_response = TransactionsSerializer(trans)
            return Response(serializer_response.data, status=status.HTTP_201_CREATED)

        return Response({'status': 'Bad request',
                         'message': 'The data that you send is invalid!'},
                        status=status.HTTP_400_BAD_REQUEST)


class UpdateTransactionState(views.APIView):

    @staticmethod
    def post(request):
        app = verify_token(request)

        serializer = TransactionsSerializerState(data=request.data)

        if serializer.is_valid():
            trans = get_object_or_404(Transactions.objects.all(), id=serializer.validated_data['transaction_id'],
                                      app=app)
            trans.state = serializer.validated_data['state']
            trans.save()
            serializer_response = TransactionsSerializer(trans)
            return Response(serializer_response.data, status=status.HTTP_200_OK)

        return Response({'status': 'Bad request',
                         'message': 'The data that you send is invalid!'},
                        status=status.HTTP_400_BAD_REQUEST)


class TrackingCode(views.APIView):

    @staticmethod
    def post(request):
        app = verify_token(request)

        serializer = TransactionTrackingCode(data=request.data)

        if serializer.is_valid():
            trans = get_object_or_404(Transactions.objects.all(), id=serializer.validated_data['transaction_id'],
                                      app=app)
            trans.tracking_code = serializer.validated_data['tracking_code']
            trans.save()
            serializer_response = TransactionsSerializer(trans)
            return Response(serializer_response.data, status=status.HTTP_200_OK)

        return Response({'status': 'Bad request',
                         'message': 'The data that you send is invalid!'},
                        status=status.HTTP_400_BAD_REQUEST)
