from django import forms
from .models import PrayBookEntry


class PrayBookForm(forms.ModelForm):
    class Meta:
        model = PrayBookEntry
        exclude = ['page']