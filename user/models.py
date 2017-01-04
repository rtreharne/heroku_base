from django.db import models
from sorl.thumbnail import ImageField
from django.contrib.auth.models import User
from conference.models import Conference

class Profile(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    conference = models.ForeignKey(Conference, blank=True, null=True)
    affiliation = models.CharField(max_length=128, blank=True, null=True)
    bio = models.CharField(max_length=140, blank=True, null=True)
    pic = ImageField(upload_to='profile', null=True, blank=True)
    twitter = models.URLField(blank=True, null=True)
    linkedIn = models.URLField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return str('{0} {1}'.format(self.user.first_name, self.user.last_name))




