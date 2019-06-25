from django.db import models 


class Event(models.Model):  
    event_image = models.FileField(verbose_name="app-logo", name=None, blank=True)
    event_name = models.CharField(max_length=30, blank=False)
    event_venue = models.CharField(max_length=30, blank=True)
    event_description = models.TextField(blank=True)
    event_start_date = models.DateField(blank=False)
    event_end_date = models.DateField(blank=False)

    def __str__(self):
        return "<Event event_name={} >".format( self.event_name, )
