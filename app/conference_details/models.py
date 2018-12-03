from django.db import models
from django.utils.translation import ugettext_lazy as _

from app.core.models import StrictTimestamp


class Conference(StrictTimestamp):
    conference_code = models.CharField(blank=False, max_length=30)
    conference_organizer = models.CharField(blank=False, max_length=30)
    conference_image = models.FileField(verbose_name="app-logo", name=None, blank=True)
    conference_name = models.CharField(max_length=30, blank=False)
    conference_location = models.CharField(max_length=30, blank=True)
    conference_description = models.TextField(blank=True)
    conference_start_date = models.DateField(blank=False)
    conference_end_date = models.DateField(blank=False)

    class Meta:
        verbose_name = _("conference_details")
        verbose_name_plural = _("conferences")

    def __str__(self):
        return "<Conference conference_name={} >".format( self.conference_name, )
