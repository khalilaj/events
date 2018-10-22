from django.db import models
from django.utils.translation import ugettext_lazy as _

from conference.core.models import StrictTimestamp


class Conference(StrictTimestamp):
    name = models.CharField(max_length=30, blank=False)
    location = models.CharField(max_length=30, blank=True)
    about = models.TextField(blank=True)
    logo = models.FileField(verbose_name="conference-logo", name=None, blank=True)

    class Meta:
        verbose_name = _("conference")
        verbose_name_plural = _("conference")
        unique_together = ("name",)

    def __str__(self):
        return "<Conference name={} >".format( self.name, )
