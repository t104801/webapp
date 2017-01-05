from django.conf.urls import url
from .views import topmenulist

urlpatterns = [
    url(r'^$', topmenulist, name='topmenu'),
        ]