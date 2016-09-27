# coding=utf-8
from rest_framework import views, status
from .models import Object, ObjectByUser
from .serializers import ObjectSerializer, ObjectCreateSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class ShowDetails(views.APIView):

    @staticmethod
    def get(request, object_id):
        serializer_response = ObjectSerializer(get_object_or_404(Object.objects.all(), id=object_id))
        return Response(serializer_response.data, status=status.HTTP_200_OK)


class ListObjects(views.APIView):

    @staticmethod
    def get(request, user):
        list_objects = [row.object for row in ObjectByUser.objects.filter(user_uuid=user)]
        serializer_response = ObjectSerializer(list_objects, many=True)
        return Response(serializer_response.data, status=status.HTTP_200_OK)


class CreateObject(views.APIView):

    @staticmethod
    def post(request):
        serializer = ObjectCreateSerializer(data=request.data)

        if serializer.is_valid():
            object_count = Object.objects.filter(url=serializer.validated_data['url']).count()

            if object_count == 1:
                serializer_response = ObjectSerializer(Object.objects.get(url=serializer.validated_data['url']))
                return Response(serializer_response.data, status=status.HTTP_302_FOUND)
            else:
                obj = Object.objects.create(name=serializer.validated_data['name'],
                                            url=serializer.validated_data['url'])
                ObjectByUser.objects.create(user_uuid=serializer.validated_data['user_uuid'],
                                            object=obj)

                serializer_response = ObjectSerializer(obj)
                return Response(serializer_response.data, status=status.HTTP_201_CREATED)

        return Response({'status': 'Bad request',
                         'message': 'The data that you send is invalid!'},
                        status=status.HTTP_400_BAD_REQUEST)
