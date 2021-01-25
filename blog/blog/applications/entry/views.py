from django.shortcuts import render
from django.views.generic import (
    ListView, DetailView
)
""" Models """
from .models import Entry, Category
# Create your views here.
class EntryListView(ListView):
    template_name = "entry/list.html"
    context_object_name = 'entries'
    paginate_by = 2

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
    
class EntryDetailView(DetailView):
    model = Entry
    template_name = "entry/detail.html"
