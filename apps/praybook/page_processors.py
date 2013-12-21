from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from mezzanine.pages.page_processors import processor_for
from .models import PrayBook, PrayBookEntry
from .forms import PrayBookForm


@processor_for(PrayBook)
def praybook(request, page):
    form = PrayBookForm()
    entries = page.praybook.entries.all().order_by('-created_at')
    paginator = Paginator(entries, 10)

    num_page = request.GET.get('page')
    try:
        entries = paginator.page(num_page)
    except PageNotAnInteger:
        entries = paginator.page(1)
    except EmptyPage:
        entries = paginator.page(paginator.num_pages)

    if request.method == 'POST':
        entries = paginator.page(1)
        entry = PrayBookEntry(page=page.praybook)

        form = PrayBookForm(request.POST, instance=entry)

        if form.is_valid():
            entry = form.save()
            form = PrayBookForm()
            return {'form': form, 'entries': entries, 'new_entry': entry}


    return {'form': form, 'entries': entries}