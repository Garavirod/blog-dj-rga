from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, View, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
""" Models """
from .models import Favorites
from applications.entry.models import Entry
# Create your views here.


class UserPageListView(LoginRequiredMixin,ListView):
    template_name = "favorites/profile.html"
    context_object_name = "entries_user"
    """ In case user isn't loggedin, redirect to """
    login_url = reverse_lazy('users_app:user-login')

    def get_queryset(self):
        return Favorites.objects.entries_user_man(self.request.user) 
    
class AddFavoritesViews(LoginRequiredMixin,View):
    login_url = reverse_lazy('users_app:user-login')
    """ Redefine post method """
    def post(self, request, *args, **kwargs):
        """ Recover user and entry by pk """
        _user = self.request.user
        pk_entry = self.kwargs['pk']
        _entry = Entry.objects.get(id=pk_entry)
        """ Add to favorites """
        Favorites.objects.create(
            user=_user,
            entry=_entry,
        )

        return HttpResponseRedirect(
            reverse(
                'favorites_app:ProfilePage',
            )
        )
class DeleteFavoriteView(DeleteView):
    model = Favorites
    success_url = '/profile'