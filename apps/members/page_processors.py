# coding: utf-8 
from __future__ import unicode_literals
from mezzanine.pages.page_processors import processor_for
from .models import MemberPage
from .forms import MemberPersonalForm, MemberAddressForm, MemberSchoolForm, MemberSpiritualForm, MemberForm


@processor_for(MemberPage)
def members_page_form(request, page):

    forms = {'personal_form': MemberPersonalForm, 'address_form': MemberAddressForm, 'school_form': MemberSchoolForm,
             'spiritual_form': MemberSpiritualForm}

    if request.method == 'POST':

        valid = True
        for form in forms:
            forms[form] = forms[form](request.POST, request.FILES)

            if not forms[form].is_valid():
                valid = False

        if valid:
            form = MemberForm(request.POST, request.FILES)
            form.save()

            forms['created'] = True

    else:
        for form in forms:
            forms[form] = forms[form]()

    return forms