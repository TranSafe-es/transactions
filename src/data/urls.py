from django.conf.urls import url
from data.views import ShowProducts

urlpatterns = [
               url(r'^show/models/(?P<id_app>.+)/(?P<id_luz>.+)/$', ShowProducts.as_view(), name="Download certificate"),
]
