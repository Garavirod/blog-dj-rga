from django.shortcuts import render
from django.views.generic import (
    ListView
)

# Create your views here.
class EntryListView(ListView):
    template_name = "entry/list.html"
    context_object_name = 'entries'
    pagination_by = 10

    def get_queryset(self):
        return []
    
