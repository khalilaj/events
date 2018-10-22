from django.conf.urls import url
from .views import EventAttendantListCreate, EventAttendantRetrieve

urlpatterns = [
    url(r'^$', EventAttendantListCreate.as_view(), name='list-create-event-attendants'),
    url(r'^(?P<pk>\d+)$', EventAttendantRetrieve.as_view(), name='retrieve-update-event-attendants'),
]