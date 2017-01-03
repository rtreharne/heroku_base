from django.shortcuts import render
from conference.models import Conference
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from .forms import MyRegistrationForm

# Create your views here.
def index(request):
    conferences = Conference.objects.all()
    return render(request, 'index.html', {'conferences': conferences})


def register_user(request, slug):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            print('Okey Dokey')

    args = {}
    args.update(csrf(request))
    args['form'] = MyRegistrationForm()
    print(args)
    return render(request, 'registration/registration_form.html', args)

