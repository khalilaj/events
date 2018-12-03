from django.conf.urls import url
from .views import SessionForumTopicListCreate, SessionForumTopicRetrieve

urlpatterns = [
    url(r'^$', SessionForumTopicListCreate.as_view(), name='list-create-session_forum_topic'),
    url(r'^(?P<pk>\d+)$', SessionForumTopicRetrieve.as_view(), name='retrieve-update-session_forum_topic'),
]