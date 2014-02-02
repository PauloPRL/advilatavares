# coding: utf-8
from __future__ import unicode_literals
from optparse import make_option
from time import sleep
from django.core.management.base import BaseCommand, CommandError
from apps.praybook.models import PrayBookEntry, UserIntercessor
from django.core.mail import send_mail


class Command(BaseCommand):
    def handle(self, **options):

        prayers = PrayBookEntry.objects.all()[0:10]
        intercessors = UserIntercessor.objects.all()

        for pray in prayers:
            for intercessor in intercessors:
                if pray.created_at > intercessor.created_at:
                    if not pray.interceded_by.filter(id=intercessor.id).exists():
                        message = '''%s

%s''' % (pray.name, pray.cause)
                        send_mail('Novo pedido de oração', message, 'no-reply@advilatavares.com.br',
                                  [intercessor.email])
                        sleep(1)