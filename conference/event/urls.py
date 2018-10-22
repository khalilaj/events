from django.conf.urls import url
from .views import EventListCreate, EventRetrieve

urlpatterns = [    
    url(r'^$', EventListCreate.as_view(), name='list-create-event'),
    url(r'^(?P<pk>\d+)$', EventRetrieve.as_view(), name='retrieve-update-event'),
]