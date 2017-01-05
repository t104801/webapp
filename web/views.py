# web/views.py
# -*- coding: UTF-8 -*-

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from .models import IrUiMenu

def topmenulist(request):
    context = {"topmenu": IrUiMenu.objects.all()}
    return render(request,
                  "web/topmenu.html",
                  context)
