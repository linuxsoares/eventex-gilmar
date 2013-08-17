# coding: utf-8

from django.contrib import admin
from eventex.core.models import Speaker, Contact, Talk

class ContactInLine(admin.TabularInline):
    model = Contact
    extra = 1

class SpeakerAdmin(admin.ModelAdmin):
    inlines = [ContactInLine,]
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(Talk)