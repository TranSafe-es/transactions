from rest_framework import permissions
from register.models import AppToken, AppRegister
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import APIException


class Forbidden(APIException):
    status_code = 403

    def __init__(self):
        super(Forbidden, self).__init__(detail="App token invalid.")


def verify_token(request):
    if 'token' not in request.GET:
        raise Forbidden()

    app_token = AppToken.objects.filter(token=request.GET.get('token', ''))

    if len(app_token) != 1:
        raise Forbidden()

    return app_token[0].app
