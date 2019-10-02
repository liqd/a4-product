from django.contrib import admin

from . import models


class SpeakupIdeaAdmin(admin.ModelAdmin):
    list_filter = ('module__project', 'module')


admin.site.register(models.SpeakupIdea, SpeakupIdeaAdmin)
