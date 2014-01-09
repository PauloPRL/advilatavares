# coding: utf-8
from __future__ import unicode_literals
from django.db import models
from mezzanine.core.fields import RichTextField
from mezzanine.pages.models import Page
from core.utils.models import AppLabel


class LinkedContent(models.Model):
    key = models.CharField(max_length=16, unique=True, null=False, blank=False)
    page = models.ForeignKey(Page, verbose_name="Página a ser linkada", null=True, blank=True)
    _title = models.CharField(max_length=255, null=True, blank=True, verbose_name="Título")
    _description = RichTextField(null=True, blank=True, verbose_name="Descrição")
    button = models.CharField(max_length=20, verbose_name="Título do botão", default="Clique aqui")

    @property
    def title(self):
        if self._title:
            return self._title
        elif self.page:
            return self.page.title
        else:
            return "Sem Título"

    @property
    def description(self):
        if self._description:
            return self._description
        elif self.page:
            return self.page.description
        else:
            return "--"

    class Meta:
        verbose_name = 'Conteúdos linkáveis'
        app_label = AppLabel("linked_content", "The stuff box")

    def __unicode__(self):
        return self.key
