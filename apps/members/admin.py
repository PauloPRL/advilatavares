# coding: utf-8 
from __future__ import unicode_literals
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from mezzanine.pages.admin import PageAdmin
from .models import Member, MemberPage


class MembersPageAdmin(PageAdmin):
    pass


class MembersAdmin(admin.ModelAdmin):
    list_display = ['cpf', 'name', 'email', 'phone', 'print_list']
    search_fields = ['name', 'cpf']

    def print_list(self, obj):
        return mark_safe('<a href="{}">Imprimir</a>'.format(reverse('print_member', kwargs={'pk': obj.pk})))

    print_list.short_description = 'Ficha cadastral'


admin.site.register(MemberPage, MembersPageAdmin)
admin.site.register(Member, MembersAdmin)