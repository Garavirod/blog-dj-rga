import datetime
#
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

""" Models """
from applications.entry.models import Entry

from django.views.generic import (
    TemplateView
)

class HomePageView(TemplateView):
    template_name = "home/index.html"
    def get_context_data(self, **kwargs):
        context = super(HomePageView,self).get_context_data(**kwargs)
        """ Cover page context """
        context["coverPage"] = Entry.objects.entry_on_coverPage() 
        return context
    
