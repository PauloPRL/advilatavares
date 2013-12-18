from django.db import models
from mezzanine.pages.models import Page


class PrayBook(Page):
    """
    Defulat page, created only for link PrayBookEntry
    """
    pass


class PrayBookEntry(models.Model):
    """
    PrayBook entries
    """
    name = models.CharField(max_length=100, verbose_name='Nome')
    email = models.EmailField(verbose_name='E-mail')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    cause = models.TextField()