from django.http import *
from django.shortcuts import *
from django.views.generic import *
from django.urls import *

class Indexview(TemplateView):
    template_name = 'Base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'CheappyBeer'
        return context