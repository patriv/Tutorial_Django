from django.shortcuts import render
from django.template import RequestContext
from django.views.generic import *


class Home(TemplateView):
    template_name = 'home.html'
