from django.shortcuts import (
    render,
    render_to_response,
    redirect
)
from django.template import RequestContext
from django.http import HttpResponseRedirect
from .models import (
    Conference,
    Deadline,
    Symposium,
    Workshop,
    Theme,
)
from .forms import ConferenceLoginForm
from django.contrib.auth import (
    authenticate,
    login,
    logout,
)
from user.models import Profile

def conf_temp(custom):
    if custom:
        return 'custom/conference.html'
    else:
        return 'conference.html'

def conference(request, slug):
    style=False
    custom=False
    conference = Conference.objects.get(slug=slug)
    deadlines = Deadline.objects.filter(conference=conference)
    guests = Profile.objects.filter(conference=conference, delegate_type='guest')
    symposia = Symposium.objects.filter(conference=conference)
    workshops = Workshop.objects.filter(conference=conference)
    return render(request, conf_temp(custom), {'conference' : conference,
                                               'deadlines'  : deadlines,
                                               'guests'     : guests,
                                               'symposia'   : symposia,
                                               'workshops'  : workshops,
                                               'style': style})

def conference_logout(request, slug):
    logout(request)
    return HttpResponseRedirect('/{0}'.format(slug))

def conference_login(request, slug):
    style=True
    logout(request)
    conference = Conference.objects.get(slug=slug)

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/{0}'.format(slug))

    login_form = ConferenceLoginForm()

    return render(request, 'registration/conference_login.html', {'form': login_form,
                                                                  'conference': conference,
                                                                  'style': style})



