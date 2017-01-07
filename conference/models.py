from __future__ import unicode_literals
from sorl.thumbnail import ImageField

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

class Symposium(models.Model):
    conference = models.ForeignKey(Conference)
    title = models.CharField(max_length=128)
    pic = models.ImageField(upload_to='symposia', null=True, blank=True)
    description = models.TextField(max_length=1000)

    def __unicode__(self):
        return '{0}: {1}'.format(self.conference, self.title)

    class Meta:
        verbose_name_plural = "Symposia"

class Theme(models.Model):
    symposium = models.ForeignKey(Symposium)
    name = models.CharField(max_length=128)
    pic = models.ImageField(upload_to='themes', null=True, blank=True)
    description = models.TextField(max_length=1000)

    def __unicode__(self):
        return str(self.symposium)

class Workshop(models.Model):
    conference = models.ForeignKey(Conference)
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=1000)
    pic = models.ImageField(upload_to='themes', null=True, blank=True)

    def __unicode__(self):
        return str(self.title)


class SocialType(models.Model):
    name = models.CharField(max_length=20)
    fa = models.CharField(max_length=25)

    def __unicode__(self):
        return str(self.name)

class SocialLink(models.Model):
    type = models.ForeignKey(SocialType)
    conference = models.ForeignKey(Conference)
    url = models.URLField()

    def __unicode__(self):
        return str('{0}:{1}'.format(self.type, self.conference))





