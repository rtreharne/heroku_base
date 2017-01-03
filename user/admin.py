from django.contrib import admin

from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ('last_name', 'first_name', 'affiliation')

admin.site.register(Profile, ProfileAdmin)
