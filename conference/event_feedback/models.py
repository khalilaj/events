from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..core.models import StrictTimestamp
from ..event.models import Event
from ..user.models import Account

class EventFeedback(StrictTimestamp):
    event_id = models.ForeignKey(Event, on_delete=models.DO_NOTHING, blank=False)
    attendant_id = models.ForeignKey(Account, on_delete=models.DO_NOTHING, blank=False)
    event_feedback = models.TextField(blank=False)

    class Meta:
        verbose_name = _('event_feedback')
        verbose_name_plural = _('event_feedback')

    def __str__(self):
        return "<EventFeedback id={} >".format(self.id)