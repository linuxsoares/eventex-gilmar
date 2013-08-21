# coding: utf-8

from django.contrib import admin
from eventex.core.models import Speaker, Contact, Talk, Media

class ContactInLine(admin.TabularInline):
    model = Contact
    extra = 1

class SpeakerAdmin(admin.ModelAdmin):
    inlines = [ContactInLine,]
    prepopulated_fields = {'slug': ('name',)}

class MediaInLine(admin.TabularInline):
    model = Media
    extra = 1

class TalkAdmin(admin.ModelAdmin):
    inlines = [MediaInLine,]


admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(Talk, TalkAdmin)
