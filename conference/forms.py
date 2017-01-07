from django import forms
from django.contrib.auth.models import User

class ConferenceLoginForm(forms.Form):
    username = forms.CharField(max_length=128, label='Username')
    password = forms.CharField(widget=forms.PasswordInput())

class ConferenceContactForm(forms.Form):
    name = forms.CharField(max_length=128)
    email = forms.EmailField()
    message = forms.CharField(max_length=12800, widget=forms.Textarea())
