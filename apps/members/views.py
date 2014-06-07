from django.views.generic import DetailView
from apps.members.models import Member


class PrintMemberView(DetailView):
    model = Member
    template_name = 'members/print.html'