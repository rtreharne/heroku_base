from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()

import user.views

urlpatterns = [
    url(r'^$', user.views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
]
