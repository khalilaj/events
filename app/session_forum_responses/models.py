from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..core.models import StrictTimestamp
from ..user.models import Account
from ..session_forum_topic.models import SessionForumTopic


class SessionForumResponses(StrictTimestamp):
    session_forum_topic_id = models.ForeignKey(SessionForumTopic, on_delete=models.DO_NOTHING, blank=False)
    session_attendant_id = models.ForeignKey(Account, on_delete=models.DO_NOTHING, blank=False)
    forum_response_msg = models.TextField(blank=False)

    class Meta:
        verbose_name = _('Session Forum Responses')
        verbose_name_plural = _('Session Forum Responses')

    def __str__(self):
        return "<SessionForumTopic forum_response_msg={} >".format(self.forum_response_msg)