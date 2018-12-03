from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from ..core.auth import JwtAuth
from .models import SessionFeedback
from .renderer import SessionFeedbackRenderer
from .serializer import ListCreateSerial, RetrieveUpdateSerial
from .permissions import SessionFeedbackPermission


class SessionFeedbackListCreate(ListCreateAPIView):

    authentication_classes = (JwtAuth, )
    renderer_classes = (SessionFeedbackRenderer,)
    permission_classes = (IsAuthenticated, SessionFeedbackPermission,)
    serializer_class = ListCreateSerial

    def get_queryset(self):
        return SessionFeedback.objects.all()


class SessionFeedbackRetrieve(RetrieveUpdateDestroyAPIView):
    
    authentication_classes = (JwtAuth, )
    renderer_classes = (SessionFeedbackRenderer,)
    permission_classes = (IsAuthenticated, SessionFeedbackPermission,)
    serializer_class = RetrieveUpdateSerial

    def get_queryset(self):
        return SessionFeedback.objects.all()