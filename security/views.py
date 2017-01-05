# -*- coding: UTF-8 -*-
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from .forms import LoginForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def dashboard(request):
    """ Display all actions by default
    actions = Action.objects.all().exclude(user=request.user)
    """
    following_ids = request.user.following.values_list('id', flat=True)
    """
    #if following_ids:
         If user is following others, retrieve only their actions
        actions = actions.filter(user_id__in=following_ids).select_related('user', 'user__profile').prefetch_related('target')
    actions = actions[:10]
    """
    return render(request, 'security/dashboard.html', {'section': 'dashboard'})#,
                                                      #'actions': actions})

