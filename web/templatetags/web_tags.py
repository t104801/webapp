from django import template
register = template.Library()

@register.simple_tag
def split(value, arg):
    print value, arg
    return value.split(',')[arg]