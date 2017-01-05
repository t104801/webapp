from django.conf.urls import url
from django.contrib.auth.views import login, \
                                      logout, \
                                      logout_then_login, \
                                      password_change, \
                                      password_change_done, \
                                      password_reset, \
                                      password_reset_done, \
                                      password_reset_confirm, \
                                      password_reset_complete
from . import views

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),

    # login / logout urls
    url(r'^login/$', view=login, name='login'),
    url(r'^logout/$', view=logout, name='logout'),
    url(r'^logout-then-login/$', view=logout_then_login, name='logout_then_login'),

    # change password urls
    url(r'^password-change/$', view=password_change, name='password_change'),
    url(r'^password-change/done/$', view=password_change_done, name='password_change_done'),

    # restore password urls
    url(r'^password-reset/$', view=password_reset, name='password_reset'),
    url(r'^password-reset/done/$', view=password_reset_done, name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', view=password_reset_confirm, name='password_reset_confirm'),
    url(r'^password-reset/complete/$', view=password_reset_complete, name='password_reset_complete'),
]