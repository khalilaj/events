from django.conf.urls import url
from .views import EventFeedbackListCreate, EventFeedbackRetrieve

urlpatterns = [    
    url(r'^$', EventFeedbackListCreate.as_view(), name='list-create-event-feedback'),
    url(r'^(?P<pk>\d+)$', EventFeedbackRetrieve.as_view(), name='retrieve-update-event-feedback'),
]