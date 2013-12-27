from mezzanine.core.fields import RichTextField
from mezzanine.pages.models import Page
from django.db import models


class Testimonial(Page):
    """
    Testimonial page
    """
    text = RichTextField(verbose_name='Texto')

    class Meta:
        verbose_name = 'Testemunho'
        verbose_name_plural = 'Testemunhos'


class TestimonialEntry(models.Model):
    """
    Testimonial Entry
    """
    name = models.CharField(max_length=100, verbose_name='Nome')
    email = models.EmailField(null=True, blank=True, verbose_name='E-mail')
    text = models.TextField(verbose_name='Testemunho')
    page = models.ForeignKey(Testimonial, related_name='entries')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)