# web/models.py
# -*- coding: UTF-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import \
    python_2_unicode_compatible

#from utils.models import CreationModificationDateMixin
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey, TreeManyToManyField

@python_2_unicode_compatible
class IrUiMenu(MPTTModel):
    """
    Model für Menustruktur mit Programmaufrufen
    """
    parent = TreeForeignKey("self", blank=True, null=True)
    name = models.CharField(_("Name"), max_length=200)
    action = models.CharField(_("Action"), max_length=200, unique=False, null=False)
    sequence = models.IntegerField(name="Sequence", unique=False, null=False,default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["tree_id", "lft"]
        verbose_name = _("Menu")
        verbose_name_plural = _("Menus")