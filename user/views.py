from django.shortcuts import render
from conference.models import Conference
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from .forms import MyRegistrationForm
from conference.models import Conference
from django.contrib.auth.models import User
from user.models import Profile
from conference.forms import ConferenceContactForm
from conference.models import SocialLink
# Create your views here.
def index(request):
    conferences = Conference.objects.all()
    return render(request, 'index.html', {'conferences': conferences})


def register_user(request, slug):
    conference = Conference.objects.get(slug=slug)
    style=True
    contact_form = ConferenceContactForm()
    social = SocialLink.objects.filter(conference=conference)

    if request.user.is_authenticated():
        return HttpResponseRedirect('/{0}/'.format(slug))

    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.latest('id')
            print(user)
            affiliation = request.POST['affiliation']
            profile = Profile(user=user, conference=conference, affiliation=affiliation)
            profile.save()


            return HttpResponseRedirect('/{0}/'.format(slug))
        else:
            args = {}
            args.update(csrf(request))
            args['form'] = form
            args['style'] = style
            args['conference'] = conference
            args['contact_form'] = contact_form
            args['social'] = social
            return render(request, 'registration/conference_registration_form.html', args)

    args = {}
    args.update(csrf(request))
    args['form'] = MyRegistrationForm()
    args['style'] = style
    args['conference'] = conference
    args['contact_form'] = contact_form
    args['social'] = social

    return render(request, 'registration/conference_registration_form.html', args)

