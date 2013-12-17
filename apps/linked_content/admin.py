from django.contrib import admin
from apps.linked_content.models import LinkedContent


class LinkedContentAdmin(admin.ModelAdmin):
    model = LinkedContent


admin.site.register(LinkedContent)