from __future__ import unicode_literals
from time import sleep
from mezzanine.blog.models import BlogPost
from mezzanine.pages.page_processors import processor_for


@processor_for('/')
def home(request, page):
    posts = BlogPost.objects.filter(status=2).order_by()[0:5]
    sleep(2)
    return {'blog_posts': posts}