# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from . import views

urlpatterns = [
   url(r'^team-list$', views.TeamListView.as_view(), name='team-list'),
   url(r'^team-edit$', views.TeamEditView.as_view(), name='team-edit'),
]
