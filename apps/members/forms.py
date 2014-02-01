# coding: utf-8 
from __future__ import unicode_literals
from django.forms import ModelForm
from .models import Member


class MemberPersonalForm(ModelForm):
    class Meta:
        model = Member
        fields = ('name', 'email', 'mobile_phone', 'phone', 'commercial_phone', 'commercial_phone_ramal', 'gender',
                  'birthday', 'marital_status', 'profession', 'gravatar',)


class MemberIdentifiationForm(ModelForm):
    class Meta:
        model = Member
        fields = ('cpf', 'rg',)


class MemberAddressForm(ModelForm):
    class Meta:
        model = Member
        fields = ('street', 'number', 'complement', 'neighboorhood', 'city', 'state', 'zip_code',)


class MemberSchoolForm(ModelForm):
    class Meta:
        model = Member
        fields = ('basic_education', 'high_school', 'college',)


class MemberSpiritualForm(ModelForm):
    class Meta:
        model = Member
        fields = ('rebirth',)


class MemberAddressForm(ModelForm):
    class Meta:
        model = Member
        fields = ('street', 'number', 'complement', 'neighboorhood', 'city', 'state', 'zip_code')


class MemberForm(ModelForm):
    class Meta:
        model = Member