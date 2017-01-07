from django.contrib import admin
from .models import (
    Conference,
    Deadline,
    Symposium,
    Theme,
    Workshop,
    SocialLink,
    SocialType,
)

class ConferenceAdmin(admin.ModelAdmin):
    model = Conference
    list_display = ('title', 'location', 'start', 'finish',)
    prepopulated_fields = {'slug': ['title'],}

class DeadlineAdmin(admin.ModelAdmin):
    model = Deadline
    list_display = ('description', 'date',)

class SymposiumAdmin(admin.ModelAdmin):
    model = Symposium
    list_display = ('title', 'conference', 'description',)

class ThemeAdmin(admin.ModelAdmin):
    model = Theme
    list_display = ('name', 'symposium')

class WorkshopAdmin(admin.ModelAdmin):
    model = Workshop
    list_display = ('title', 'conference')



admin.site.register(Conference, ConferenceAdmin)
admin.site.register(Deadline, DeadlineAdmin)
admin.site.register(Symposium, SymposiumAdmin)
admin.site.register(Theme, ThemeAdmin)
admin.site.register(Workshop, WorkshopAdmin)
admin.site.register(SocialLink)
admin.site.register(SocialType)