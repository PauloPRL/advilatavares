from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import Agenda, Event


class EventTabularInline(admin.TabularInline):
    model = Event


class AgendaAdmin(PageAdmin):
    inlines = (EventTabularInline,)


class EventAdmin(admin.ModelAdmin):
    pass


admin.site.register(Agenda, AgendaAdmin)
admin.site.register(Event, EventAdmin)