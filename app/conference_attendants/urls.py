from django.conf.urls import url

from .views import ConferenceAttendantsListCreate, ConferenceAttendantsRetrieve

urlpatterns = [    
    url(r'^$', ConferenceAttendantsListCreate.as_view(), name='list-create-conference_attendants'),
    url(r'^(?P<pk>\d+)$', ConferenceAttendantsRetrieve.as_view(), name='retrieve-update-conference_attendants'),
]