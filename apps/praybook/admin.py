from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import PrayBook, PrayBookEntry, Intercessor, UserIntercessor


class PrayBookAdmin(PageAdmin):
    pass


class PrayBookEntryAdmin(admin.ModelAdmin):
    pass


class IntercessorAdmin(PageAdmin):
    pass


class UserIntercessorAdmin(admin.ModelAdmin):
    pass

admin.site.register(PrayBook, PrayBookAdmin)
admin.site.register(PrayBookEntry, PrayBookEntryAdmin)
admin.site.register(Intercessor, IntercessorAdmin)
admin.site.register(UserIntercessor, UserIntercessorAdmin)