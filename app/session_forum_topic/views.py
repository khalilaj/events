from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from ..core.auth import JwtAuth
from .models import SessionForumTopic
from .renderer import SessionForumTopicRenderer
from .serializer import RetrieveUpdateSerial, ListCreateSerial
from .permissions import SessionForumTopicPermission


class SessionForumTopicListCreate(ListCreateAPIView):

    authentication_classes = (JwtAuth, )
    renderer_classes = (SessionForumTopicRenderer,)
    permission_classes = (IsAuthenticated, SessionForumTopicPermission,)
    serializer_class = ListCreateSerial

    def get_queryset(self):
        return SessionForumTopic.objects.all()


class SessionForumTopicRetrieve(RetrieveUpdateDestroyAPIView):
    
    authentication_classes = (JwtAuth, )
    renderer_classes = (SessionForumTopicRenderer,)
    permission_classes = (IsAuthenticated, SessionForumTopicPermission)
    serializer_class = RetrieveUpdateSerial

    def get_queryset(self):
        return SessionForumTopic.objects.all()

