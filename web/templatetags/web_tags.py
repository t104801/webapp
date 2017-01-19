from django import template
from django.utils.safestring import mark_safe, SafeData
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def split_as_option(value, splitter='|', position=0, autoescape=None):
    print splitter
    if not isinstance(value, SafeData):
        value = mark_safe(value)
    value = value.split(splitter)[0]

    return mark_safe(value)

split_as_option.is_safe = True
split_as_option.needs_autoescape = True