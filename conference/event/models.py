from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..conference.models import Conference
from ..core.models import StrictTimestamp
from ..user.models import Account

class Event(StrictTimestamp):
    speaker = models.ForeignKey(Account, on_delete=models.DO_NOTHING, blank=False)
    name = models.CharField(max_length=30, blank=False)
    description = models.TextField(max_length=30, blank=False)
    startTime = models.DateTimeField(blank=False)
    endTime = models.DateTimeField(blank=False)
    conference_id = models.ForeignKey(Conference, on_delete=None, blank=False)


    class Meta:
        verbose_name = _('event')
        verbose_name_plural = _('events')

    def __str__(self):
        return "<Event name={} >".format(self.name)