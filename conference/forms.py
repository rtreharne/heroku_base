from django import forms

class ConferenceLoginForm(forms.Form):
    username = forms.CharField(max_length=128, label='Username')
    password = forms.CharField(widget=forms.PasswordInput())