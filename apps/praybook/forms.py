from django import forms
from .models import PrayBookEntry, UserIntercessor


class PrayBookForm(forms.ModelForm):
    class Meta:
        model = PrayBookEntry
        exclude = ['page']


class IntercessorForm(forms.ModelForm):
    class Meta:
        model = UserIntercessor
        exclude = ['status', 'received_entries']