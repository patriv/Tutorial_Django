#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from home.models import *


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

        labels = {
            'first_name': 'Nombre',
            'last_name' : 'Apellido',
        }


    def clean(self):
        data = self.cleaned_data
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        return data