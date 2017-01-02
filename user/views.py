from django.shortcuts import render
from conference.models import Conference
from django.http import HttpResponse

# Create your views here.
def index(request):
    conferences = Conference.objects.all()
    return render(request, 'index.html', {'conferences': conferences})

