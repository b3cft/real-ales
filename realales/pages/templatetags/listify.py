from django.template import Library
from django.core.urlresolvers import reverse
import string

register = Library()

@register.simple_tag
def searchLinks():
    letters=''
    for letter in string.ascii_lowercase:
        letters += '<li><a href="'+reverse('brewery_startswith', args=[letter])+'">'+letter+'</a></li>'
    return letters