# movies/admin.py
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
#from django_mptt_admin.admin import DjangoMpttAdmin
from mptt_tree_editor.admin import TreeEditor
from .models import IrUiMenu

class IrUiMenuAdmin(TreeEditor):
    list_display = ["name", "action"]
    list_filter = ["name"]


admin.site.register(IrUiMenu, IrUiMenuAdmin)