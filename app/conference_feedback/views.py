from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import ConferenceFeedback
from ..core.auth import JwtAuth
from .renderer import ConferenceFeedbackRenderer
from .serializer import ListCreateSerial, RetrieveUpdateSerial
from .permissions import ConferenceFeedbackPermission


class ConferenceFeedbackListCreate(ListCreateAPIView):

    authentication_classes = (JwtAuth, )
    renderer_classes = (ConferenceFeedbackRenderer,)
    permission_classes = (IsAuthenticated, ConferenceFeedbackPermission,)
    serializer_class = ListCreateSerial

    def get_queryset(self):
        return ConferenceFeedback.objects.all()


class ConferenceFeedbackRetrieve(RetrieveUpdateDestroyAPIView):
    
    authentication_classes = (JwtAuth, )
    renderer_classes = (ConferenceFeedbackRenderer,)
    permission_classes = (IsAuthenticated, ConferenceFeedbackPermission,)
    serializer_class = RetrieveUpdateSerial

    def get_queryset(self):
        return ConferenceFeedback.objects.all()