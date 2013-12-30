# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from mezzanine.core.fields import RichTextField
from mezzanine.pages.models import Page
from django.db import models


class Agenda(Page):
    class Meta:
        verbose_name = 'Agenda'


class Event(models.Model):
    title = models.CharField(max_length=100, verbose_name='Título')
    description = RichTextField(verbose_name='Descrição')
    is_paid = models.BooleanField(verbose_name='É pago?', default=False)
    vacancies = models.IntegerField(verbose_name='Número de vagas', null=True, blank=True)
    date = models.DateTimeField()
    agenda = models.ForeignKey(Agenda)

    def __unicode__(self):
        return str(self.date) + ' - ' + self.title

