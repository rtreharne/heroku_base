from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import (
    password_reset,
    password_reset_done,
    password_reset_complete,
    password_reset_confirm,
)
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()

import user.views

urlpatterns = [

    url(r'^accounts/password/reset/$', password_reset, {'template_name': 'registration/password_reset_form.html'}, name="password_reset"),
    url(r'^accounts/password/reset/done/$', password_reset_done, {'template_name': 'registration/password_reset_done.html'}, name="password_reset_done"),
    # the below should all be on one line
    url(r'^accounts/password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', password_reset_confirm, {'template_name': 'registration/password_reset_confirm.html'}, name="password_reset_confirm"),
    url(r'^accounts/password/done/$', password_reset_complete, {'template_name': 'registration/password_reset_complete.html'}, name="password_reset_complete"),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^$', user.views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('conference.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
