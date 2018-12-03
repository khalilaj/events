from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..core.models import StrictTimestamp
from ..session.models import Session
from ..user.models import Account


class SessionFeedback(StrictTimestamp):
    session_id = models.ForeignKey(Session, on_delete=models.DO_NOTHING, blank=False)
    session_attendant_id = models.ForeignKey(Account, on_delete=models.DO_NOTHING, blank=False)
    session_feedback_msg = models.TextField(blank=False)

    class Meta:
        verbose_name = _('Session Feedback')
        verbose_name_plural = _('Session Feedback')

    def __str__(self):
        return "<SessionFeedback session_feedback_msg={} >".format(self.session_feedback_msg)