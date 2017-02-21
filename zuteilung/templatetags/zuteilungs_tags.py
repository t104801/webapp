# zuteilungen/zuteilungs_tags.py
# -*- coding: UTF-8 -*-

from django import template

register = template.Library()

@register.filter
def in_filialid(lwabe, id):
    #print lwabe, id
    return lwabe.filter(filiale=id)
