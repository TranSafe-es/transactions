from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
from data.urls import urlpatterns as dataurls
from objects.urls import urlpatterns as objectsurls

urlpatterns = [
               url(r'^admin/', include(admin.site.urls)),
               url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

               # pages
               url(r'^api/v1/transaction/', include(dataurls)),
               url(r'^api/v1/object/', include(objectsurls)),

               url('^.*$', TemplateView.as_view(template_name='index.html'), name='index')
               ]
