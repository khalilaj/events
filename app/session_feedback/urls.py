from django.conf.urls import url
from .views import SessionFeedbackListCreate, SessionFeedbackRetrieve

urlpatterns = [    
    url(r'^$', SessionFeedbackListCreate.as_view(), name='list-create-session_feedback'),
    url(r'^(?P<pk>\d+)$', SessionFeedbackRetrieve.as_view(), name='retrieve-update-session_feedback'),
]