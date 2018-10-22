from django.conf.urls import url
from .views import EventSpeakerListCreate, EventSpeakerRetrieve

urlpatterns = [
    url(r'^$', EventSpeakerListCreate.as_view(), name='list-create-event'),
    url(r'^(?P<pk>\d+)$', EventSpeakerRetrieve.as_view(), name='retrieve-update-event'),
]