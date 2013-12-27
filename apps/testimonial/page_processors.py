from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from mezzanine.pages.page_processors import processor_for
from .models import Testimonial, TestimonialEntry
from .forms import TestimonialForm


@processor_for(Testimonial)
def testimonial(request, page):
    form = TestimonialForm()
    entries = page.testimonial.entries.all().order_by('-created_at')
    paginator = Paginator(entries, 1)

    num_page = request.GET.get('page')
    try:
        entries = paginator.page(num_page)
    except PageNotAnInteger:
        entries = paginator.page(1)
    except EmptyPage:
        entries = paginator.page(paginator.num_pages)

    ret = {'form': form, 'entries': entries}

    if request.method == 'POST':
        entries = paginator.page(1)
        entry = TestimonialEntry(page=page.testimonial)

        form = TestimonialForm(request.POST, instance=entry)
        ret['form'] = form

        if form.is_valid():
            form.save()

            entries = page.testimonial.entries.all().order_by('-created_at')
            paginator = Paginator(entries, 1)
            entries = paginator.page(1)

            form = TestimonialForm()

            ret['entries'] = entries
            ret['form'] = form

    return ret