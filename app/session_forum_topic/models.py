from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..core.models import StrictTimestamp
from ..session.models import Session
from ..user.models import Account


class SessionForumTopic(StrictTimestamp):
    session_id = models.ForeignKey(Session, on_delete=models.DO_NOTHING, blank=False)
    session_speaker_id = models.ForeignKey(Account, on_delete=models.DO_NOTHING, blank=False)
    forum_topic_msg = models.TextField(blank=False)

    class Meta:
        verbose_name = _('Session Forum Topic')
        verbose_name_plural = _('Session Forum Topics')

    def __str__(self):
        return "<SessionForumTopic forum_topic_msg={} >".format(self.forum_topic_msg)