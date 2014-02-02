# coding: utf-8
from __future__ import unicode_literals
from django.db.models import CharField, ImageField, Model, PositiveIntegerField, ForeignKey
from mezzanine.core.models import Orderable
from mezzanine.pages.models import Page


class Slider(Model):
    title = CharField(max_length=50, verbose_name='Título do Slider', null=True, blank=True)
    page = ForeignKey(Page, verbose_name='Página', help_text='Selecione a página que o slider deve aparecer, deixe em '
                                                             'branco, caso deva aparecer na home',
                      related_name='slider')

    def __unicode__(self):
        return self.title


class Slide(Orderable):
    title = CharField(max_length=50, verbose_name='Título', null=True, blank=True)
    description = CharField(max_length=256, verbose_name='Descrição', null=True, blank=True)
    image = ImageField(upload_to='slides', verbose_name='Imagem')
    time = PositiveIntegerField(default=5, verbose_name='Tempo visível', help_text='Em segundos')
    slider = ForeignKey(Slider, related_name='slides')