# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from mezzanine.core.fields import RichTextField
from mezzanine.pages.models import Page


class LinkedContent(models.Model):
    key = models.CharField(max_length=16, unique=True, null=False, blank=False)
    page = models.ForeignKey(Page, verbose_name="Página a ser linkada", null=True)
    _title = models.CharField(max_length=255, null=True, blank=True, verbose_name="Título")
    _description = RichTextField(null=True, blank=True, verbose_name="Descrição")
    button = models.CharField(max_length=20, verbose_name="Título do botão", default="Clique aqui")

    @property
    def title(self):
        return self._title or self.page.title

    @property
    def description(self):
        return self._description or self.page.description

    class Meta:
        verbose_name='Conteúdos linkável'

    def __unicode__(self):
        return self.key