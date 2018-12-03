from django.utils.translation import ugettext_lazy as _
from django.db import models

from ..core.models import StrictTimestamp


class Tag(StrictTimestamp):
    tag_name = models.CharField(max_length=30, blank=False)

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')

    def __str__(self):
        return "<Tag tag_name={} >".format(self.tag_name)