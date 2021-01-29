from django.urls import path
from . import views

app_name = 'entry_app'

urlpatterns = [
    path(
        'entries-list',
        views.EntryListView.as_view(),
        name='EntriesList'
    ),
    path(
        'detail-entry/<slug>/', #search data in model based on its slug filed 
        views.EntryDetailView.as_view(),
        name='DetailEntry'
    ),
]
