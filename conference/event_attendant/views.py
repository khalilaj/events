from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import EventAttendant
from ..core.auth import JwtAuth
from .renderer import EventAttendantRenderer
from .serializer import RetrieveUpdateSerial, ListCreateSerial


class EventAttendantListCreate(ListCreateAPIView):
    authentication_classes = (JwtAuth,)
    renderer_classes = (EventAttendantRenderer,)
    permission_classes = (IsAuthenticated,)
    serializer_class = ListCreateSerial

    def get_queryset(self):
        return EventAttendant.objects.all()


class EventAttendantRetrieve(RetrieveUpdateDestroyAPIView):
    authentication_classes = (JwtAuth,)
    renderer_classes = (EventAttendantRenderer,)
    permission_classes = (IsAuthenticated,)
    serializer_class = RetrieveUpdateSerial

    def get_queryset(self):
        return EventAttendant.objects.all()

