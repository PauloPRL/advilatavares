# coding: utf-8 
from __future__ import unicode_literals
from mezzanine.pages.page_processors import processor_for
from .models import MemberPage
from .forms import MemberPersonalForm, MemberIdentifiationForm, MemberAddressForm, MemberSchoolForm, MemberSpiritualForm


@processor_for(MemberPage)
def members_page_form(request, page):
    print 'Teste'
    return {'personal_form': MemberPersonalForm(), 'identification_form': MemberIdentifiationForm(),
            'address_form': MemberAddressForm(), 'school_form': MemberSchoolForm(),
            'spiritual_form': MemberSpiritualForm()}