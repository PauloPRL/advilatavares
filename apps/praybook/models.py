# -*- coding: utf-8
from __future__ import unicode_literals
from django.db import models
from mezzanine.core.fields import RichTextField
from mezzanine.pages.models import Page


class PrayBook(Page):
    """
    Default page, created only for link PrayBookEntry
    """
    text = RichTextField(verbose_name="Texto")

    class Meta:
        verbose_name = "Livro de Oração"
        verbose_name_plural = "Livros de Orações"


class Intercessor(Page):
    """
    Default page, created only for link PrayBookEntry
    """
    text = RichTextField(verbose_name="Texto")

    class Meta:
        verbose_name = "Intercessor"
        verbose_name_plural = "Intercessores"


class PrayBookEntry(models.Model):
    """
    PrayBook entries
    """
    name = models.CharField(max_length=100, verbose_name='Nome')
    email = models.EmailField(verbose_name='E-mail', null=True, blank=True)
    cause = models.TextField(verbose_name='Causa')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    page = models.ForeignKey(PrayBook, related_name='entries')

    def __unicode__(self):
        return self.name + ': ' + self.cause[0:150]


class UserIntercessor(models.Model):
    """
    An intercessor for pray entries
    """
    name = models.CharField(max_length=100, verbose_name='Nome')
    email = models.EmailField(verbose_name='E-mail')
    received_entries = models.ManyToManyField(PrayBookEntry, verbose_name='Pedidos Recebidos')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Intercessor'
        verbose_name_plural = 'Intercessores'

    def __unicode__(self):
        return self.name + ', ' + self.email