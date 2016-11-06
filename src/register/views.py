# coding=utf-8
from rest_framework import views, status
from .models import AppRegister, AppToken
from .serializers import RegisterAppSerializer, TokenAppSerializer
from rest_framework.response import Response


class RegisterApp(views.APIView):

    @staticmethod
    def post(request):
        serializer = RegisterAppSerializer(data=request.data)

        if serializer.is_valid():
            apps_count = AppRegister.objects.filter(name=serializer.validated_data['name']).count()

            if apps_count == 1:
                app = AppRegister.objects.get(name=serializer.validated_data["name"])
            else:
                app = AppRegister.objects.create(name=serializer.validated_data["name"])

            AppToken.objects.filter(app=app).delete()
            token = AppToken.objects.create(app=app)
            serializer_response = TokenAppSerializer(token)
            return Response(serializer_response.data, status=status.HTTP_200_OK)

        return Response({'status': 'Bad request',
                         'message': 'The data that you send is invalid!'},
                        status=status.HTTP_400_BAD_REQUEST)
