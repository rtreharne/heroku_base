from __future__ import unicode_literals

from django.db import models

class Conference(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)
    location = models.CharField(max_length=128)
    start = models.DateTimeField()
    finish = models.DateTimeField()

    def __unicode__(self):
        return str(self.title)

class Deadline(models.Model):
    conference = models.ForeignKey(Conference)
    description = models.CharField(max_length=128, help_text="e.g. Early Bird Registration")
    date = models.DateTimeField()

    def __unicode__(self):
        return str(self.description)

