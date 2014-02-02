from __future__ import unicode_literals
from mezzanine.blog.models import BlogPost
from mezzanine.pages.page_processors import processor_for


@processor_for('/')
def home(request, page):
    posts = BlogPost.objects.filter(status=2).order_by()[0:3]
    print('-' * 30)
    print posts

    return {'blog_posts': posts}