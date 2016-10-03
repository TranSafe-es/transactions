from django.conf.urls import url
from .views import ShowDetails, ListObjects, CreateObject

urlpatterns = [
               url(r'^details/(?P<object_id>.+)/$', ShowDetails.as_view(), name="Show details"),
               url(r'^list/(?P<identifier>.+)/$', ListObjects.as_view(), name="List objects"),
               url(r'^new/$', CreateObject.as_view(), name="Create object"),
]
