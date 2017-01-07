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
    SocialLink
)
from .forms import ConferenceLoginForm, ConferenceContactForm
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
    committee = Profile.objects.filter(conference=conference, delegate_type='committee')
    symposia = Symposium.objects.filter(conference=conference)
    workshops = Workshop.objects.filter(conference=conference)
    contact_form = ConferenceContactForm()
    social_links = SocialLink.objects.filter(conference=conference)
    print(social_links)
    return render(request, conf_temp(custom), {'conference' : conference,
                                               'deadlines'  : deadlines,
                                               'guests'     : guests,
                                               'committee'   : committee,
                                               'symposia'   : symposia,
                                               'workshops'  : workshops,
                                               'contact_form': contact_form,
                                               'social'     : social_links,
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



