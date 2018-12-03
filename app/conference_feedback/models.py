from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..core.models import StrictTimestamp
from ..conference_details.models import Conference
from ..user.models import Account


class ConferenceFeedback(StrictTimestamp):
    conference_id = models.ForeignKey(Conference, on_delete=models.DO_NOTHING, blank=False)
    conference_attendant_id = models.ForeignKey(Account, on_delete=models.DO_NOTHING, blank=False)
    conference_feedback_msg = models.TextField(blank=False)

    class Meta:
        verbose_name = _('Conference Feedback')
        verbose_name_plural = _('Conference Feedback')

    def __str__(self):
        return "<ConferenceFeedback conference_feedback_msg={} >".format(self.conference_feedback_msg)