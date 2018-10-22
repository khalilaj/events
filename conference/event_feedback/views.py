from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import EventFeedback
from ..core.auth import JwtAuth
from .renderer import EventFeedbackRenderer
from .serializer import ListCreateSerial, RetrieveUpdateSerial


class EventFeedbackListCreate(ListCreateAPIView):

    authentication_classes = (JwtAuth, )
    renderer_classes = (EventFeedbackRenderer,)
    permission_classes = (IsAuthenticated, )
    serializer_class = ListCreateSerial

    def get_queryset(self):
        return EventFeedback.objects.all()


class EventFeedbackRetrieve(RetrieveUpdateDestroyAPIView):
    
    authentication_classes = (JwtAuth, )
    renderer_classes = (EventFeedbackRenderer, )
    permission_classes = (IsAuthenticated, )
    serializer_class = RetrieveUpdateSerial

    def get_queryset(self):
        return EventFeedback.objects.filter(attendant=self.request.user.id)

