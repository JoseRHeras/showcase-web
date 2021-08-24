from django import template
from landing_page.models import SocialPlatforms

register = template.Library()


@register.inclusion_tag('base/footer.html')
def social_media_footer():
    links = SocialPlatforms.objects.all()
    return {'links' : links}