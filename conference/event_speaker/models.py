from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..core.models import StrictTimestamp
from ..event.models import Event
from ..user.models import Account

class EventSpeaker(StrictTimestamp):
    event_id = models.ForeignKey(Event, on_delete=models.DO_NOTHING, blank=False)
    event_speaker_id = models.ForeignKey(Account, on_delete=models.DO_NOTHING, blank=False)

    class Meta:
        verbose_name = _('event_speaker')
        verbose_name_plural = _('event_speaker')

    def __str__(self):
        return "<EventSpeaker id={} >".format(self.id)