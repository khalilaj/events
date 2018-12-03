from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import SessionMaterial
from ..core.auth import JwtAuth
from .renderer import SessionMaterialRenderer
from .serializer import RetrieveUpdateSerial, ListCreateSerial
from .permissions import SessionMaterialPermission


class SessionMaterialListCreate(ListCreateAPIView):

    authentication_classes = (JwtAuth, )
    renderer_classes = (SessionMaterialRenderer,)
    permission_classes = (IsAuthenticated, SessionMaterialPermission,)
    serializer_class = ListCreateSerial

    def get_queryset(self):
        return SessionMaterial.objects.all()


class SessionMaterialRetrieve(RetrieveUpdateDestroyAPIView):
    
    authentication_classes = (JwtAuth, )
    renderer_classes = (SessionMaterialRenderer,)
    permission_classes = (IsAuthenticated, SessionMaterialPermission)
    serializer_class = RetrieveUpdateSerial

    def get_queryset(self):
        return SessionMaterial.objects.all()

