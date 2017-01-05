# movies/admin.py
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import IrUiMenu

class IrUiMenuAdmin(DjangoMpttAdmin):
    list_display = ["name", "action"]
    list_filter = ["name"]


admin.site.register(IrUiMenu, IrUiMenuAdmin)