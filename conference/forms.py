from django import forms
from django.contrib.auth.models import User

class ConferenceLoginForm(forms.Form):
    username = forms.CharField(max_length=128, label='Username')
    password = forms.CharField(widget=forms.PasswordInput())

