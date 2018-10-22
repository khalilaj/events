from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import EventSpeaker
from ..core.auth import JwtAuth
from .renderer import EventSpeakerRenderer
from .serializer import RetrieveUpdateSerial, ListCreateSerial


class EventSpeakerListCreate(ListCreateAPIView):
    authentication_classes = (JwtAuth,)
    renderer_classes = (EventSpeakerRenderer,)
    permission_classes = (IsAuthenticated,)
    serializer_class = ListCreateSerial

    def get_queryset(self):
        return EventSpeaker.objects.all()


class EventSpeakerRetrieve(RetrieveUpdateDestroyAPIView):
    authentication_classes = (JwtAuth,)
    renderer_classes = (EventSpeakerRenderer,)
    permission_classes = (IsAuthenticated,)
    serializer_class = RetrieveUpdateSerial

    def get_queryset(self):
        return EventSpeaker.objects.all()

