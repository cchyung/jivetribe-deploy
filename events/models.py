from __future__ import unicode_literals

from django.db import models
from cms.models import CMSPlugin

class Event(models.Model):
    name = models.CharField(max_length=250, help_text="Name of the event.")
    description = models.CharField(max_length=500, help_text="Description.")
    location = models.CharField(max_length=500, help_text = 'Location of event.')
    url = models.CharField(max_length=500, help_text = 'link to event website', blank = True)
    date = models.DateTimeField()
    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['-date']

class EventPluginModel(CMSPlugin):
    event = models.ForeignKey(Event)
    def __str__(self):
        return self.event.name

