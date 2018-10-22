from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Event
from ..core.auth import JwtAuth
from .renderer import EventRenderer
from .serializer import RetrieveUpdateSerial, ListCreateSerial


class EventListCreate(ListCreateAPIView):

    authentication_classes = (JwtAuth, )
    renderer_classes = (EventRenderer,)
    permission_classes = (IsAuthenticated, )
    serializer_class = ListCreateSerial

    def get_queryset(self):
        return Event.objects.all()


class EventRetrieve(RetrieveUpdateDestroyAPIView):
    
    authentication_classes = (JwtAuth, )
    renderer_classes = (EventRenderer, )
    permission_classes = (IsAuthenticated, )
    serializer_class = RetrieveUpdateSerial

    def get_queryset(self):
        return Event.objects.all()

