from typing import final
from django import template
from apps.landing_page.models import SocialPlatforms

register = template.Library()


@register.inclusion_tag('base/footer.html', name='footer')
def social_media_footer():

    links = SocialPlatforms.objects.all()
    return {'links' : links}



@register.inclusion_tag('base/navbar.html', name="navbar", takes_context=True)
def navbar(context):
    path = context.request.path
    navbar_active = {
        'home':  'active'if path == '/' else '',
        'project': 'active'if path == '/projects' else '',
        'resume': 'active'if path == '/resume' else ''
    }

    return {'links': navbar_active}
