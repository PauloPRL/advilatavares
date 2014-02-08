# coding: utf-8
from __future__ import unicode_literals
import datetime
from django.utils.timezone import now
from mezzanine.pages.page_processors import processor_for
from .models import Agenda, Event
from dateutil.relativedelta import relativedelta


@processor_for(Agenda)
def agenda(request, page):
    today = now()
    month = int(request.GET.get('month', 0))
    date = today + relativedelta(months=month)


    return {'events': Event.objects.filter(agenda=page.agenda, date__year=date.year, date__month=date.month).order_by('date'),
            'date':date, 'month': month}