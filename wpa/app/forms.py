# -*- coding: utf-8 -*-

from django import forms

class TeamLogoForm(forms.Form):
    file = forms.FileField(label='Selectionner un logo')
