# coding: utf-8
from __future__ import unicode_literals
from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from apps.praybook.models import PrayBookEntry, UserIntercessor


class Command(BaseCommand):
    def handle(self, **options):

        prayers = PrayBookEntry.objects.all()[0:10]
        intercessors = UserIntercessor.objects.all()

        for pray in prayers:
             for intercessor in intercessors:
                 if not intercessor.received_entries.filter(pray).exists():
                     print 'O pedido %s não foi recebido pelo usuário %s' % (pray, intercessor)