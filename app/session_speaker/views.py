from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from ..core.auth import JwtAuth
from .models import SessionSpeaker
from .renderer import SessionSpeakerRenderer
from .serializer import RetrieveUpdateSerial, ListCreateSerial
from .permissions import SessionSpeakerPermission


class SessionSpeakerListCreate(ListCreateAPIView):
    authentication_classes = (JwtAuth,)
    renderer_classes = (SessionSpeakerRenderer,)
    permission_classes = (IsAuthenticated, SessionSpeakerPermission,)
    serializer_class = ListCreateSerial

    def get_queryset(self):
        return SessionSpeaker.objects.all()


class SessionSpeakerRetrieve(RetrieveUpdateDestroyAPIView):
    authentication_classes = (JwtAuth,)
    renderer_classes = (SessionSpeakerRenderer,)
    permission_classes = (IsAuthenticated, SessionSpeakerPermission, )
    serializer_class = RetrieveUpdateSerial

    def get_queryset(self):
        return SessionSpeaker.objects.all()
