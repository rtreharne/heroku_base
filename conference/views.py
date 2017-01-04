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

def conference(request, slug):
    style=True
    conference = Conference.objects.get(slug=slug)
    deadlines = Deadline.objects.filter(conference=conference)
    symposia = Symposium.objects.filter(conference=conference)
    workshops = Workshop.objects.filter(conference=conference)
    return render(request, 'custom/conference.html', {'conference' : conference,
                                               'deadlines'  : deadlines,
                                               'symposia'   : symposia,
                                               'workshops'  : workshops,
                                               'style': style})

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



