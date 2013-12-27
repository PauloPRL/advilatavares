from mezzanine.pages.admin import PageAdmin
from django.contrib import admin
from .models import Testimonial, TestimonialEntry


class TestimonialAdmin(PageAdmin):
    pass


class TestimonialEntryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(TestimonialEntry, TestimonialEntryAdmin)