from django.conf.urls import url
from .views import SessionAttendantListCreate, SessionAttendantRetrieve

urlpatterns = [
    url(r'^$', SessionAttendantListCreate.as_view(), name='list-create-session_attendants'),
    url(r'^(?P<pk>\d+)$', SessionAttendantRetrieve.as_view(), name='retrieve-update-session_attendants'),
]