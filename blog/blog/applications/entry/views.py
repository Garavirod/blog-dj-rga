from django.shortcuts import render
from django.views.generic import (
    ListView
)
""" Models """
from .models import Entry, Category
# Create your views here.
class EntryListView(ListView):
    template_name = "entry/list.html"
    context_object_name = 'entries'
    pagination_by = 10

    """ for send a context into any view based on class @override get_context_data """
    def get_context_data(self, **kwargs):
        context = super(EntryListView, self).get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context
    

    def get_queryset(self):
        """ This request is sending through url """
        keyword = self.request.GET.get('keyword','')
        category = self.request.GET.get('category','')
        """ query """
        result = Entry.objects.SearchEntry(keyword,category)
        return result
    
