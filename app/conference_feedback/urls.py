from django.conf.urls import url
from .views import ConferenceFeedbackListCreate, ConferenceFeedbackRetrieve

urlpatterns = [    
    url(r'^$', ConferenceFeedbackListCreate.as_view(), name='list-create-conference_feedback'),
    url(r'^(?P<pk>\d+)$', ConferenceFeedbackRetrieve.as_view(), name='retrieve-update-conference_feedback'),
]