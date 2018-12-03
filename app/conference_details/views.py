from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from ..core.auth import JwtAuth
from .models import Conference
from .serializer import RetrieveUpdateSerial, ListCreateSerial
from .renderer import ConferenceRenderer
from .permissions import ConferencePermission


class ConferenceListCreate(ListCreateAPIView):

    authentication_classes = (JwtAuth,)
    permission_classes = (IsAuthenticated,ConferencePermission,)
    renderer_classes = (ConferenceRenderer,)
    serializer_class = ListCreateSerial

    def get_queryset(self):
        return Conference.objects.all()


class ConferenceRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):

    authentication_classes = (JwtAuth,)
    permission_classes = (IsAuthenticated,ConferencePermission,)
    serializer_class = RetrieveUpdateSerial

    def get_queryset(self):
        return Conference.objects.all()
