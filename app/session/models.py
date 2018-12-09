from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..core.models import StrictTimestamp
from ..conference_details.models import Conference
from ..user.models import Account
from ..tag.models import Tag


class Session(StrictTimestamp):
    conference_id = models.ForeignKey(Conference, on_delete=models.DO_NOTHING, blank=False)
    session_speaker_id = models.ForeignKey(Account, on_delete=models.DO_NOTHING, blank=True, null=True)
    session_tag_id = models.ForeignKey(Tag,  on_delete=models.DO_NOTHING, blank=True, null=True)

    session_name = models.CharField(max_length=30, blank=False)
    session_description = models.TextField(blank=True)
    session_location = models.CharField(blank=True, max_length=30)
    session_startTime = models.DateTimeField(blank=False)
    session_endTime = models.DateTimeField(blank=False)
    session_image = models.FileField(verbose_name="app-logo", name=None, blank=True)


    class Meta:
        verbose_name = _('Session')
        verbose_name_plural = _('Sessions')

    def __str__(self):
        return "<Session session_name={} >".format(self.session_name)