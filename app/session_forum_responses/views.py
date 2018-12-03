from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from ..core.auth import JwtAuth
from .models import SessionForumResponses
from .renderer import SessionForumResponsesRenderer
from .serializer import RetrieveUpdateSerial, ListCreateSerial
from .permissions import SessionForumResponsesPermission


class SessionForumResponsesListCreate(ListCreateAPIView):

    authentication_classes = (JwtAuth, )
    renderer_classes = (SessionForumResponsesRenderer,)
    permission_classes = (IsAuthenticated, SessionForumResponsesPermission,)
    serializer_class = ListCreateSerial

    def get_queryset(self):
        return SessionForumResponses.objects.all()


class SessionForumResponsesRetrieve(RetrieveUpdateDestroyAPIView):
    
    authentication_classes = (JwtAuth, )
    renderer_classes = (SessionForumResponsesRenderer,)
    permission_classes = (IsAuthenticated, SessionForumResponsesPermission)
    serializer_class = RetrieveUpdateSerial

    def get_queryset(self):
        return SessionForumResponses.objects.all()

