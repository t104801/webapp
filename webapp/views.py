# webapp/views.py
#  -*- coding: UTF-8 -*-

from django.utils.datastructures import MultiValueDictKeyError
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.template import RequestContext
from web.models import IrUiMenu
import json


def index(request):
    topmenus = IrUiMenu.topmenu()
    submenus = []

    try:
        action = request.GET["action"]
    except MultiValueDictKeyError:
        action = None

    if action == None:
        submenus = []
    else:
        submenus = IrUiMenu.get_descendants(IrUiMenu.objects.get(pk=action)).order_by("lft")

    print topmenus, "/", submenus
    return render(request,
                  'index.html',
                  {"topmenus": topmenus,
                   "submenus": submenus},
                  )


def show_json(request):
    response_data = dict()
    response_data['result'] = 'failed'
    response_data['message'] = 'you messed up'
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def webapp(request):
    print request
    return render(request, 'index.html')
