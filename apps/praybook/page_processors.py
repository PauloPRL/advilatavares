from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404
from mezzanine.pages.page_processors import processor_for
from .models import PrayBook, PrayBookEntry, Intercessor, UserIntercessor
from .forms import PrayBookForm, IntercessorForm


@processor_for(PrayBook)
def praybook(request, page):
    form = PrayBookForm()
    intercessor_form = IntercessorForm()
    entries = page.praybook.entries.all().order_by('-created_at')
    paginator = Paginator(entries, 10)

    num_page = request.GET.get('page')
    try:
        entries = paginator.page(num_page)
    except PageNotAnInteger:
        entries = paginator.page(1)
    except EmptyPage:
        entries = paginator.page(paginator.num_pages)

    ret = {'form': form, 'entries': entries, 'intercessor_form': intercessor_form}

    if request.method == 'POST':
        entries = paginator.page(1)
        entry = PrayBookEntry(page=page.praybook)

        form = PrayBookForm(request.POST, instance=entry)
        ret['form'] = form

        if form.is_valid():
            entry = form.save()
            form = PrayBookForm()

            ret['entries'] = entries
            ret['new_entry'] = entry
            ret['form'] = form

    return ret


@processor_for(Intercessor)
def intercessor(request, page):
    if request.method == 'POST':
        form = IntercessorForm(request.POST)

        if form.is_valid():
            form.save()
            return {'created': True}

        return {'created': False, 'form': form}
    else:
        raise Http404