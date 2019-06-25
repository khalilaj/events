from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from ..core.auth import JwtAuth
from .models import Event
from .serializer import RetrieveUpdateSerial, ListCreateSerial
from .renderer import Renderer 


class ListCreate(ListCreateAPIView):

    authentication_classes = (JwtAuth,)
    permission_classes = (AllowAny,)
    renderer_classes = (Renderer,)
    serializer_class = ListCreateSerial

    def get_queryset(self):
        return Event.objects.all()


class RetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):

    authentication_classes = (JwtAuth,)
    permission_classes = (IsAuthenticated,)
    serializer_class = RetrieveUpdateSerial

    def get_queryset(self):
        return Event.objects.all()
