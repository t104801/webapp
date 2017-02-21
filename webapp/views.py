# webapp/views.py
#  -*- coding: UTF-8 -*-

from django.utils.datastructures import MultiValueDictKeyError
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.template import RequestContext
import json

def index(request):
    return render(request,
                  'index.html',
                  {},
                  )

def show_json(request):
    response_data = dict()
    response_data['result'] = 'failed'
    response_data['message'] = 'you messed up'
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def webapp(request):
    print request
    return render(request, 'index.html')
