from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..core.models import StrictTimestamp
from ..conference_details.models import Conference
from ..user.models import Account


class ConferenceAttendants(StrictTimestamp):
    conference = models.ForeignKey(Conference, on_delete=models.DO_NOTHING, blank=False, null=False)
    conference_attendant_id = models.ForeignKey(Account, on_delete=models.DO_NOTHING, blank=False, null=False)
    attendants_status = models.BooleanField(blank=False, default=False)

    class Meta:
        verbose_name = _('Conference Attendant')
        verbose_name_plural = _('Conference Attendants')

    def __str__(self):
        return "<ConferenceAttendants attendants_status={} >".format(self.attendants_status, )