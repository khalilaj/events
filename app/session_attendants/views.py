from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from ..core.auth import JwtAuth
from .models import SessionAttendants
from .renderer import SessionAttendantsRenderer
from .serializer import RetrieveUpdateSerial, ListCreateSerial
from .permissions import SessionAttendantsPermission


class SessionAttendantListCreate(ListCreateAPIView):
    authentication_classes = (JwtAuth,)
    renderer_classes = (SessionAttendantsRenderer,)
    permission_classes = (IsAuthenticated, SessionAttendantsPermission,)
    serializer_class = ListCreateSerial

    def get_queryset(self):
            return SessionAttendants.objects.all()


class SessionAttendantRetrieve(RetrieveUpdateDestroyAPIView):
    authentication_classes = (JwtAuth,)
    renderer_classes = (SessionAttendantsRenderer, SessionAttendantsPermission,)
    permission_classes = (IsAuthenticated,)
    serializer_class = RetrieveUpdateSerial

    def get_queryset(self):
        return SessionAttendants.objects.all()