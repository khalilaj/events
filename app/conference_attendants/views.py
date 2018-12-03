from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from ..core.auth import JwtAuth
from .models import ConferenceAttendants
from .renderer import ConferenceAttendantsRenderer
from .serializer import ListCreateSerial, RetrieveUpdateSerial
from .permissions import ConferenceAttendantsPermission


class ConferenceAttendantsListCreate(ListCreateAPIView):

    authentication_classes = (JwtAuth, )
    renderer_classes = (ConferenceAttendantsRenderer,)
    permission_classes = (IsAuthenticated, ConferenceAttendantsPermission,)
    serializer_class = ListCreateSerial

    def get_queryset(self):
        return ConferenceAttendants.objects.all()


class ConferenceAttendantsRetrieve(RetrieveUpdateDestroyAPIView):
    
    authentication_classes = (JwtAuth, )
    renderer_classes = (ConferenceAttendantsRenderer,)
    permission_classes = (IsAuthenticated, ConferenceAttendantsPermission,)
    serializer_class = RetrieveUpdateSerial

    def get_queryset(self):
        return ConferenceAttendants.objects.all()
