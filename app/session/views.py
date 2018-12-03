from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from ..core.auth import JwtAuth
from .models import Session
from .renderer import SessionRenderer
from .serializer import RetrieveUpdateSerial, ListCreateSerial
from .permissions import SessionPermission


class SessionListCreate(ListCreateAPIView):

    authentication_classes = (JwtAuth, )
    renderer_classes = (SessionRenderer,)
    permission_classes = (IsAuthenticated, SessionPermission,)
    serializer_class = ListCreateSerial

    def get_queryset(self):
        return Session.objects.all()


class SessionRetrieve(RetrieveUpdateDestroyAPIView):
    
    authentication_classes = (JwtAuth, )
    renderer_classes = (SessionRenderer,)
    permission_classes = (IsAuthenticated, SessionPermission)
    serializer_class = RetrieveUpdateSerial

    def get_queryset(self):
        return Session.objects.all()

