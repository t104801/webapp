# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.template import RequestContext
from django.conf import settings
import json

def index(request):
	sett = settings.BASE_DIR
	return render(request, 'index.html', {'sett': sett})

def show_json(request):
	response_data = dict()
	response_data['result'] = 'failed'
	response_data['message'] = 'you messed up'
	return HttpResponse(json.dumps(response_data), content_type="application/json")

def webapp(request):
	sett = settings.BASE_DIR
	print request
	return render(request, 'index.html', {'sett': sett})