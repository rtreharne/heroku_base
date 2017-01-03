from django.db import models
from sorl.thumbnail import ImageField
from django.contrib.auth.models import User
from conference.models import Conference

class Profile(models.Model):
    user = models.ForeignKey(User)
    conference = models.ForeignKey(Conference, blank=True, null=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    affiliation = models.CharField(max_length=128)
    bio = models.CharField(max_length=140, blank=True, null=True)
    pic = ImageField(upload_to='profile', null=True, blank=True)
    twitter = models.URLField(blank=True, null=True)
    linkedIn = models.URLField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return str('{0} {1}'.format(self.first_name, self.last_name))




