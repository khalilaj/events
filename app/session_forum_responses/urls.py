from django.conf.urls import url
from .views import SessionForumResponsesListCreate, SessionForumResponsesRetrieve

urlpatterns = [
    url(r'^$', SessionForumResponsesListCreate.as_view(), name='list-create-session_forum_responses'),
    url(r'^(?P<pk>\d+)$', SessionForumResponsesRetrieve.as_view(), name='retrieve-update-session_forum_responses'),
]