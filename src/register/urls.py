from django.conf.urls import url
from .views import RegisterApp

urlpatterns = [
               url(r'^app/$', RegisterApp.as_view(), name="Register app"),
]