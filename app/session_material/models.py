from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..core.models import StrictTimestamp
from ..session.models import Session


class SessionMaterial(StrictTimestamp):
    title = models.CharField(blank=False, max_length=30)
    session_id = models.ForeignKey(Session, on_delete=models.DO_NOTHING, blank=False)
    session_material = models.FileField(blank=False)
    session_material_description = models.TextField(blank=False)


    class Meta:
        verbose_name = _('Session Material')
        verbose_name_plural = _('Session Materials')

    def __str__(self):
        return "<SessionMaterial title={} >".format(self.title)