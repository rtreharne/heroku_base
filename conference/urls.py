from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

import conference.views

urlpatterns = [

    url(r'^(?P<slug>[-\w]+)/$', conference.views.conference, name="conference"),
    url(r'^(?P<slug>[-\w]+)/login/$', conference.views.conference_login, name="conference_login"),
    url(r'^(?P<slug>[-\w]+)/logout/$', conference.views.conference_login, name="conference_logout"),
]