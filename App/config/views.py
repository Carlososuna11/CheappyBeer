from django.http import *
from django.shortcuts import *
from django.views.generic import *
from django.urls import *

class Indexview(TemplateView):
    template_name = 'index.html'