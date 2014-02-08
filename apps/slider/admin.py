from django.contrib import admin
from mezzanine.core.admin import TabularDynamicInlineAdmin
from .models import Slide, Slider


class SlideAdmin(TabularDynamicInlineAdmin):
    model = Slide


class SliderAdmin(admin.ModelAdmin):
    inlines = (SlideAdmin,)


admin.site.register(Slider, SliderAdmin)