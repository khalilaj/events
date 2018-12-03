from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _

from ..core.models import StrictTimestamp
from ..session.models import Session
from ..user.models import Account


class SessionSpeaker(StrictTimestamp):
    session_id = models.ForeignKey(Session, on_delete=models.DO_NOTHING, blank=False)
    session_speaker_id = models.ForeignKey(Account, on_delete=models.DO_NOTHING, blank=True, null=True)

    def create_session_speaker(weak=False, **kwargs):
        if kwargs['instance'].session_speaker_id:
            session_speaker_id = kwargs['instance'].session_speaker_id

            session_speaker = SessionSpeaker.objects.create(session_id=kwargs['instance'],session_speaker_id= session_speaker_id)

    post_save.connect(create_session_speaker, sender=Session, )

    class Meta:
        verbose_name = _('Session Speaker')
        verbose_name_plural = _('Session Speakers')

    def __str__(self):
        return "<Session_speaker id={} >".format(self.id)