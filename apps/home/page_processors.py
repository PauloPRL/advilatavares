from mezzanine.pages.page_processors import processor_for
from ..agenda.models import Event
from ..agenda.utils import get_days_in_week


@processor_for('/')
def home(request, page):
    days = get_days_in_week()
    events = Event.objects.filter(date__range=(days[0], days[-1]))

    agenda = []
    for day in days:
        tmp = {'date': day, 'events': []}
        for event in events:
            if event.date.day == day.day:
                tmp['events'].append(event)

        agenda.append(tmp)

    return {'agenda': agenda}