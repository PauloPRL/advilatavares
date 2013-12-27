from django import forms
from .models import TestimonialEntry


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = TestimonialEntry
        exclude = ['page']