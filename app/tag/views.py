from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from ..core.auth import JwtAuth
from .models import Tag
from .renderer import TagRenderer
from .serializer import RetrieveUpdateSerial, ListCreateSerial
from .permissions import TagPermission


class TagListCreate(ListCreateAPIView):

    authentication_classes = (JwtAuth, )
    renderer_classes = (TagRenderer,)
    permission_classes = (IsAuthenticated, TagPermission,)
    serializer_class = ListCreateSerial

    def get_queryset(self):
        return Tag.objects.all()


class TagRetrieve(RetrieveUpdateDestroyAPIView):
    
    authentication_classes = (JwtAuth, )
    renderer_classes = (TagRenderer,)
    permission_classes = (IsAuthenticated, TagPermission)
    serializer_class = RetrieveUpdateSerial

    def get_queryset(self):
        return Tag.objects.all()

