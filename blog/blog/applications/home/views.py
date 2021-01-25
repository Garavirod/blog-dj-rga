import datetime
#
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

""" Models """
from applications.entry.models import Entry
from .models import Home
""" FormsModel """
from .forms import SubscriptorForm, ContactForm
from django.views.generic import (
    TemplateView,
    CreateView
)

class HomePageView(TemplateView):
    template_name = "home/index.html"
    def get_context_data(self, **kwargs):
        context = super(HomePageView,self).get_context_data(**kwargs)
        """ load home """
        context['home'] = Home.objects.latest('created')
        """ Cover page context """
        context["coverPage"] = Entry.objects.entry_on_coverPage() 
        """ Cover page articles context"""
        context["articles"] = Entry.objects.entry_articles()
        """ Recent articles context """
        context["recentArticles"] = Entry.objects.entry_recent_articles()
        """ Send subscriptor form """
        context["subsForm"]= SubscriptorForm
        return context
    
class SubscriptorCreateView(CreateView):
    """ FromModel linked """
    form_class = SubscriptorForm
    """ URL in case register were success """
    success_url = '.' # '.' Same page

class ContactCreateView(CreateView):
    """ FromModel linked """
    form_class = ContactForm
    """ URL in case register were success """
    success_url = '.' # '.' Same page
