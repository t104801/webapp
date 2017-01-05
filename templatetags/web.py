from django import template
from django.template.loader import get_template
from django.template.base import FilterExpression

from ..sitetreeapp import get_sitetree

register = template.Library()

# All utility methods are implemented in SiteTree class
sitetree = get_sitetree()
