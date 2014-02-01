# coding: utf-8 
from __future__ import unicode_literals
from django.db import models
from mezzanine.core.fields import RichTextField
from mezzanine.pages.models import Page


class MemberPage(Page):
    text = RichTextField(verbose_name='Texto')


class Member(models.Model):

    GENDER_CHOICE = (
        ('m', 'Masculino'),
        ('f', 'Feminino'),
    )

    MARITAL_STATUS_CHOICES = (
        ('single', 'Solteiro',),
        ('married', 'Casado',),
        ('divorced', 'Divorciado',),
        ('widowed', 'Viuvo',),
    )

    STATE_CHOICES = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranão'),
        ('MG', 'Minas Gerais'),
        ('MS', 'Mato Grosso do Sul'),
        ('MT', 'Mato Grosso'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PE', 'Pernanbuco'),
        ('PI', 'Piauí'),
        ('PR', 'Paraná'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('RS', 'Rio Grande do Sul'),
        ('SC', 'Santa Catarina'),
        ('SE', 'Sergipe'),
        ('SP', 'São Paulo'),
        ('TO', 'Tocantins')
    )

    SCHOOL_CHOICES = (
        ('none', 'Não cursou'),
        ('incomplete', 'Incompleto'),
        ('complete', 'Completo'),
    )

    # Personal Data
    name = models.CharField(verbose_name='Nome completo', max_length=120)
    email = models.EmailField(verbose_name='E-mail', null=True, blank=True)
    mobile_phone = models.CharField(verbose_name='Celular', max_length=15, null=True, blank=True)
    phone = models.CharField(verbose_name='Telefone', max_length=15)
    commercial_phone = models.CharField(verbose_name='Telefone Comercial', max_length=14, null=True, blank=True)
    commercial_phone_ramal = models.CharField(verbose_name='Ramal', max_length=7, null=True, blank=True)
    gender = models.CharField(verbose_name='Sexo', choices=GENDER_CHOICE, default=GENDER_CHOICE[0][0], max_length=1)
    birthday = models.DateField(verbose_name='Nascimento')
    marital_status = models.CharField(verbose_name='Estado civil', choices=MARITAL_STATUS_CHOICES,
                                      default=MARITAL_STATUS_CHOICES[0][0], max_length=7)
    profession = models.CharField(verbose_name='Profissão', max_length=100, null=True, blank=True)
    gravatar = models.ImageField(verbose_name='Foto 3x4', null=True, blank=True, upload_to='members')

    # Identification DATA
    cpf = models.CharField(verbose_name='CPF', max_length=14, null=True, blank=True)
    rg = models.CharField(verbose_name='RG', max_length=15, null=True, blank=True)

    # Address Data
    street = models.CharField(verbose_name='Logradouro', max_length=30)
    number = models.CharField(verbose_name='Número', max_length=9)
    complement = models.CharField(verbose_name='Complemento', max_length='20', null=True, blank=True)
    neighborhood = models.CharField(verbose_name='Bairro', max_length=30)
    city = models.CharField(verbose_name='Cidade', max_length=30)
    state = models.CharField(verbose_name='Estado', choices=STATE_CHOICES, default='SP', max_length=2)
    zip_code = models.CharField(verbose_name='CEP', max_length=8)

    # School
    basic_education = models.CharField(verbose_name='Ensino Fundamental', choices=SCHOOL_CHOICES,
                                       default=SCHOOL_CHOICES[0][0], max_length=10)
    high_school = models.CharField(verbose_name='Ensino Médio', choices=SCHOOL_CHOICES, default=SCHOOL_CHOICES[0][0],
                                   max_length=10)
    college = models.CharField(verbose_name='Ensino Superior', choices=SCHOOL_CHOICES, default=SCHOOL_CHOICES[0][0],
                               max_length=10)

    # Spiritual
    rebirth = models.BooleanField(verbose_name='É Batizado nas águas?')