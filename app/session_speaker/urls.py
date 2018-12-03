from django.conf.urls import url
from .views import SessionSpeakerListCreate, SessionSpeakerRetrieve

urlpatterns = [
    url(r'^$', SessionSpeakerListCreate.as_view(), name='list-create-session_speaker'),
    url(r'^(?P<pk>\d+)$', SessionSpeakerRetrieve.as_view(), name='retrieve-update-session_speaker'),
]