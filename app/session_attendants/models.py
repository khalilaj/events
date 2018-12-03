from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..core.models import StrictTimestamp
from ..session.models import Session
from ..user.models import Account


class SessionAttendants(StrictTimestamp):
    session_id = models.ForeignKey(Session, on_delete=models.DO_NOTHING, blank=False, null=False)
    session_attendant_id = models.ForeignKey(Account, on_delete=models.DO_NOTHING, blank=False, null=False)
    session_attendance_status = models.BooleanField(default=False, blank=False)

    class Meta:
        verbose_name = _('Session Attendant')
        verbose_name_plural = _('Session Attendants')

    def __str__(self):
        return "<SessionAttendants session_attendance_status={} >".format(self.session_attendance_status)
