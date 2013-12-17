from mezzanine import template
from django.template import Context
from django.template.loader import get_template
from apps.linked_content.models import LinkedContent


register = template.Library()


@register.render_tag
def linked_content(context, token):

        stoken = token.split_contents()
        key = stoken[1]

        if len(stoken) > 2:
            template_location = stoken[2]
        else:
            template_location = "includes/linked_content.html"

        context['content'] = LinkedContent.objects.get_or_create(key=key)[0]
        t = get_template(template_location)
        return t.render(context)