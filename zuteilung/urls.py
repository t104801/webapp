# zuteilungen/urls.py
# -*- coding: UTF-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    # zuteilungs views
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$',
        views.ZuBaseFilNrList.as_view(),
        name='filial_list'),
    url(r'^$', views.ZuBaseFilNrList.as_view(), name='filial_list'),
    ]