from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import PrayBook, PrayBookEntry


class PrayBookAdmin(PageAdmin):
    pass


class PrayBookEntryAdmin(admin.ModelAdmin):
    pass

admin.site.register(PrayBook, PrayBookAdmin)
admin.site.register(PrayBookEntry, PrayBookEntryAdmin)