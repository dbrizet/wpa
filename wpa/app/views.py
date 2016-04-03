from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import View

from app.models import Team

class TeamListView(ListView):
    model = Team
    template_name = 'team_list.html'

class TeamEditView(CreateView):
    model = Team
    template_name = 'team_edit.html'
    fields = ['name']

    def get_success_url(self):
        return reverse('team-list')
