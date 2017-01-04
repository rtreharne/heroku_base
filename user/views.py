from django.shortcuts import render
from conference.models import Conference
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from .forms import MyRegistrationForm
from conference.models import Conference

# Create your views here.
def index(request):
    conferences = Conference.objects.all()
    return render(request, 'index.html', {'conferences': conferences})


def register_user(request, slug):
    conference = Conference.objects.get(slug=slug)
    style=True
    if request.user.is_authenticated():
        return HttpResponseRedirect('/{0}/'.format(slug))

    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/{0}/'.format(slug))
        else:
            print(form.errors)

    args = {}
    args.update(csrf(request))
    args['form'] = MyRegistrationForm()
    args['style'] = style
    args['conference'] = conference
    print(args)
    return render(request, 'registration/conference_registration_form.html', args)

