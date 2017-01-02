from django.contrib import admin
from .models import (
    Conference,
    Deadline
)

class ConferenceAdmin(admin.ModelAdmin):
    model = Conference
    list_display = ('title', 'location', 'start', 'finish',)
    prepopulated_fields = {'slug': ['title'],}

class DeadlineAdmin(admin.ModelAdmin):
    model = Deadline
    list_display = ('description', 'date',)

admin.site.register(Conference, ConferenceAdmin)
admin.site.register(Deadline, DeadlineAdmin)
