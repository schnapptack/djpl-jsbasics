from django import template
from django.utils.safestring import mark_safe
import json

register = template.Library()

@register.filter
def inlinejson(value):
    """
    python json dumps function does not escape forward slashes.
    This creates problems when embedding json blobs inside scripts and
    opens up XSS security holes!
    Use this filter to create proper blobs to use in inline javascripts.
    """
    return mark_safe(json.dumps(value).replace('/', '\\/'))


@register.filter
def escapeinlinejson(value):
    """
    python json dumps function does not escape forward slashes.
    This creates problems when embedding json blobs inside scripts and
    opens up XSS security holes!
    Use this filter to create proper blobs to use in inline javascripts.
    """
    return mark_safe(value.replace('/', '\\/'))
