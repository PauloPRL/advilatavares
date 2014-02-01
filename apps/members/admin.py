# coding: utf-8 
from __future__ import unicode_literals
from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import Member, MemberPage


class MembersPageAdmin(PageAdmin):
    pass


class MembersAdmin(admin.ModelAdmin):
    pass


admin.site.register(MemberPage, MembersPageAdmin)
admin.site.register(Member, MembersAdmin)