from django.shortcuts import render
from .models import Conference, Deadline
from .forms import ConferenceLoginForm

def conference(request, slug):
    conference = Conference.objects.get(slug=slug)
    deadlines = Deadline.objects.filter(conference=conference)
    return render(request, 'conference.html', {'conference': conference,
                                               'deadlines': deadlines})

def login(request, slug):
    login_form = ConferenceLoginForm()
    conference = Conference.objects.get(slug=slug)
    return render(request, 'registration/conference_login.html', {'conference': conference,
                                                                  'form': login_form})


